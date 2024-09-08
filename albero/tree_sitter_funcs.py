from logging import Logger

from token_tools import Token, merge_tokens
from tree_sitter import Node, Parser, Tree, TreeCursor


def node_to_tokens(
    root_node: Node | Tree, mapping: dict[str, str], logger: Logger
) -> list[Token]:
    cursor: TreeCursor = root_node.walk()
    tokens: list[Token] = []
    visited_nodes: set = set()

    while True:
        node: Node | None = cursor.node
        if not node:
            break

        # Avoid re-processing the same node
        if node.id in visited_nodes:
            if cursor.goto_first_child():
                continue
            if cursor.goto_next_sibling():
                continue

            moved = False
            while cursor.goto_parent():
                if cursor.goto_next_sibling():
                    moved = True
                    break

            if moved:
                continue
            break

        visited_nodes.add(node.id)

        if node.child_count != 0 and node.type != "ERROR":
            continue

        if node.type not in mapping:
            fail_string = f'Node type "{node.type}" not mapped. Start point: {node.start_point}, end point: {node.end_point}'
            logger.warning(fail_string)
            continue

        start_row, start_col = node.start_point
        end_row, end_col = node.end_point

        if end_row == start_row:
            token_pos: tuple[int, int] = (start_row + 1, start_col)
            token_len: int = end_col - start_col
            token: Token = (token_pos, token_len, mapping[node.type])
            tokens.append(token)
            continue

        split_text = node.text.splitlines()  # type: ignore
        for i, line in enumerate(split_text):
            if line.strip() == b"":
                continue

            if i == 0:
                token_pos: tuple[int, int] = (start_row + 1, start_col)
                token: Token = (token_pos, len(line), mapping[node.type])
                tokens.append(token)
                continue

            token_len: int = len(line.lstrip())
            start_col: int = len(line) - token_len
            token_pos: tuple[int, int] = (start_row + 1 + i, start_col)
            token: Token = (token_pos, token_len, mapping[node.type])
            tokens.append(token)

    return merge_tokens(tokens)


def edit_tree(
    old_code: str, new_code: str, tree: Tree, parser: Parser
) -> Tree:
    if old_code == new_code:
        return tree

    old_code_lines = old_code.splitlines()
    new_code_lines = new_code.splitlines()

    # Find the first differing line
    def find_first_diff(old_lines, new_lines):
        min_len = min(len(old_lines), len(new_lines))
        for i in range(min_len):
            if old_lines[i] != new_lines[i]:
                return i
        return min_len

    # Find the last differing line
    def find_last_diff(old_lines, new_lines):
        min_len = min(len(old_lines), len(new_lines))
        for i in range(1, min_len + 1):
            if old_lines[-i] != new_lines[-i]:
                return len(old_lines) - i
        return min_len

    # Get line diffs
    first_diff = find_first_diff(old_code_lines, new_code_lines)
    last_diff_old = find_last_diff(old_code_lines, new_code_lines)
    last_diff_new = find_last_diff(new_code_lines, old_code_lines)

    # Calculate byte offsets
    start_byte = sum(len(line) + 1 for line in old_code_lines[:first_diff])
    old_end_byte = sum(
        len(line) + 1 for line in old_code_lines[: last_diff_old + 1]
    )
    new_end_byte = sum(
        len(line) + 1 for line in new_code_lines[: last_diff_new + 1]
    )

    # Edit the tree
    tree.edit(
        start_byte=start_byte,
        old_end_byte=old_end_byte,
        new_end_byte=new_end_byte,
        start_point=(first_diff, 0),
        old_end_point=(
            last_diff_old,
            len(old_code_lines[last_diff_old]) if old_code_lines else 0,
        ),
        new_end_point=(
            last_diff_new,
            len(new_code_lines[last_diff_new]) if new_code_lines else 0,
        ),
    )

    # Reparse the tree from the start_byte
    tree = parser.parse(bytes(new_code, "utf8"), tree)
    return tree
