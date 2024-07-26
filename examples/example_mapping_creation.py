from logging import INFO, Logger, basicConfig, getLogger

from tree_sitter import Language

from albero import GENERIC_TOKENS, Token, TreeSitterHighlighter, get_lang

# Logging
basicConfig(
    level=INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger: Logger = getLogger("Main")

# Useful stuff for highlighting
archaic_lang: Language = get_lang("archaic_language")
print(GENERIC_TOKENS)
custom_mapping: dict[str, str] = {
    "xyz_tree_sitter_stuff": "token_in_generic_tokens"  # See python mapping in albero source
}

# Highlighting
highlighter = TreeSitterHighlighter()

highlighter.add_language("archaic_language", archaic_lang, {})
highlighter.update_mapping("archaic_language", custom_mapping)
highlighter.add_file("test", "archaic_language")
highlighter.update_file("test", "def test(): ...")

tokens: list[Token] = highlighter.get_highlights("test")
# The logger will print out tree sitter token types not found in the mapping
# and these can be added manually as found best fitting.
