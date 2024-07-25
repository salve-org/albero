from tree_sitter_python import language as python_language  # noqa: F401

python_mapping: dict[str, str] = {
    "comment": "Comment",
    "_": "Keyword",
    "as": "Keyword",
    "break": "Keyword",
    "case": "Keyword",
    "class": "Keyword",
    "continue": "Keyword",
    "def": "Keyword",
    "elif": "Keyword",
    "else": "Keyword",
    "false": "Keyword",
    "for": "Keyword",
    "from": "Keyword",
    "if": "Keyword",
    "import": "Keyword",
    "in": "Keyword",
    "is": "Keyword",
    "is not": "Keyword",
    "lambda": "Keyword",
    "match": "Keyword",
    "none": "Keyword",
    "not": "Keyword",
    "not in": "Keyword",
    "pass": "Keyword",
    "raise": "Keyword",
    "return": "Keyword",
    "true": "Keyword",
    "while": "Keyword",
    "@": "Name",
    "identifier": "Name",
    "float": "Number",
    "integer": "Number",
    "!=": "Operator",
    "*": "Operator",
    "**": "Operator",
    "*=": "Operator",
    "**=": "Operator",
    "+": "Operator",
    "+=": "Operator",
    "-": "Operator",
    "-=": "Operator",
    "->": "Operator",
    "/": "Operator",
    "/=": "Operator",
    "<": "Operator",
    "<=": "Operator",
    "=": "Operator",
    "==": "Operator",
    ">": "Operator",
    ">=": "Operator",
    "and": "Operator",
    "ellipsis": "Operator",
    "or": "Operator",
    "|": "Operator",
    "(": "Punctuation",
    ")": "Punctuation",
    ",": "Punctuation",
    ".": "Punctuation",
    ":": "Punctuation",
    "[": "Punctuation",
    "]": "Punctuation",
    "{": "Punctuation",
    "}": "Punctuation",
    "escape_sequence": "String",
    "string": "String",
    "string_content": "String",
    "string_end": "String",
    "string_start": "String",
}


# print(
#     {
#         k: v
#         for k, v in sorted(
#             python_mapping.items(), key=lambda item: (item[1], item)
#         )
#     }
# )
