from tree_sitter import Language

from albero import Token, TreeSitterHighlighter, get_lang, get_mapping


def test_example_usage():
    py_lang: Language = get_lang("python")
    mapping: dict[str, str] = get_mapping("python")

    highlighter = TreeSitterHighlighter()

    highlighter.add_language("python", py_lang, mapping)
    highlighter.update_file(
        "test", "python", "def test(): pass"
    )  # Trying to add a file with a language not in the system gives an Exception

    tokens: list[Token] = highlighter.get_highlights(
        "test"
    )  # Trying to use a file not in the system gives an Exception

    highlighter.remove_file("test")
    highlighter.remove_language(
        "python"
    )  # Can be done first but it will already auto-close any files that use it

    assert tokens == []
