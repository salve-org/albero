Token = tuple[tuple[int, int], int, str]

generic_tokens: list[str] = [
    "Whitespace",
    "Text",
    "Error",
    "Keyword",
    "Name",
    "String",
    "Number",
    "Literal",
    "Operator",
    "Punctuation",
    "Comment",
    "Generic",
]


def only_tokens_in_text_range(
    tokens: list[Token], text_range: tuple[int, int]
) -> list[Token]:
    # We create a new list because lists are pass by reference
    output_tokens: list[Token] = []

    for token in tokens:
        token_lineno: int = token[0][0]
        minimum_line: int = text_range[0]
        maximum_line: int = text_range[1]

        if token_lineno < minimum_line or token_lineno > maximum_line:
            continue

        output_tokens.append(token)

    output_tokens = merge_tokens(output_tokens)
    return output_tokens


def merge_tokens(tokens: list[Token]) -> list[Token]:
    output_tokens: list[Token] = []
    depth: int = 0
    for token in tokens:
        # Deal with basic edge case
        if depth == 0:
            output_tokens.append(token)
            depth += 1
            continue

        previous_token = output_tokens[-1]

        # Get our boolean checks
        same_token_type: bool = previous_token[2] == token[2]
        same_line: bool = previous_token[0][0] == token[0][0]
        neighboring_tokens: bool = (
            previous_token[0][1] + previous_token[1] == token[0][1]
        )

        # Determine if tokens should be merged
        if not (same_token_type and same_line and neighboring_tokens):
            output_tokens.append(token)
            depth += 1
            continue

        # Replace previous token with new token (we don't increase depth because we are substituting, not adding)
        new_token: Token = (
            (token[0][0], previous_token[0][1]),
            previous_token[1] + token[1],
            token[2],
        )
        output_tokens[-1] = new_token
    return output_tokens
