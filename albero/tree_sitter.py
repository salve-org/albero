from logging import Logger, getLogger

from tree_sitter import Language, Parser, Tree

from .misc import normal_text_range
from .tokens import Token, only_tokens_in_text_range
from .tree_sitter_funcs import edit_tree, node_to_tokens

trees_and_parsers: dict[str, tuple[Tree, Parser, str]] = {}


def tree_sitter_highlight(
    new_code: str,
    language_str: str,
    logger: Logger,
    mapping: dict[str, str] | None = None,
    language_parser: Parser | None = None,
    text_range: tuple[int, int] = (1, -1),
) -> list[Token]:
    tree: Tree
    return_tokens: list[Token]

    if not mapping:
        # Fallback on the custom implementation
        raise Exception("No mapping provided!")

    split_text, text_range = normal_text_range(new_code, text_range)

    if language_str not in trees_and_parsers:
        if not language_parser:
            # We will never get here, the IPC API will deal with these but we need to appease
            # the static type checkers
            return []

        tree = language_parser.parse(bytes(new_code, "utf8"))
        trees_and_parsers[language_str] = (tree, language_parser, new_code)
        return_tokens = node_to_tokens(tree.root_node, mapping, logger)
        return_tokens = only_tokens_in_text_range(return_tokens, text_range)
        return return_tokens

    tree, parser, old_code = trees_and_parsers[language_str]
    new_tree = edit_tree(old_code, new_code, tree, parser)
    trees_and_parsers[language_str] = (new_tree, parser, new_code)

    return_tokens = node_to_tokens(new_tree, mapping, logger)
    return_tokens = only_tokens_in_text_range(return_tokens, text_range)
    return return_tokens


TreeAndParser = tuple[Tree, Parser, str]  # Tree, Parser, code


class TreeSitterHighlighter:
    def __init__(self) -> None:
        self.files: dict[
            str, tuple[str, TreeAndParser]
        ] = {}  # filename, tuple[file lanugage type, TreeAndParser]
        self.mappings: dict[str, dict[str, str]] = {}
        self.logger = getLogger("TreeSitterHighlighter")

    def add_language(
        self, language_name: str, language: Language, mapping: dict[str, str]
    ) -> None: ...
    def update_mapping(
        self, language_name: str, mapping: dict[str, str]
    ) -> None: ...
    def update_file(
        self, file_name: str, language_name: str, code: str
    ) -> None: ...
    def get_highlights(self, file_name: str) -> list[Token]:
        return []

    def remove_file(self, file_name: str) -> None: ...
    def remove_language(self, language_name: str) -> None: ...
