from sys import platform

from tree_sitter import Language

from albero import (
    Token,
    TreeSitterHighlighter,
    get_lang,
    get_mapping,
    lang_from_so,
)

py_lang: Language = get_lang("python")
mapping: dict[str, str] = get_mapping("python")


def test_basic_usage():
    highlighter = TreeSitterHighlighter()

    highlighter.add_language("python", py_lang, mapping)
    highlighter.add_file(
        "test", "python"
    )  # Trying to add a file with a language not in the system gives an AlberoException
    highlighter.update_file(
        "test", "def test(): ..."
    )  # Trying to update a file not in the system gives an AlberoException

    tokens: list[Token] = highlighter.get_highlights(
        "test"
    )  # Trying to use a file not in the system gives an AlberoException

    assert tokens == [
        ((1, 0), 3, "Keyword"),
        ((1, 4), 4, "Name"),
        ((1, 8), 3, "Punctuation"),
        ((1, 12), 3, "Operator"),
    ]


def test_file_removal():
    highlighter = TreeSitterHighlighter()

    highlighter.add_language("python", py_lang, mapping)
    highlighter.add_file(
        "test", "python"
    )  # Trying to add a file with a language not in the system gives an AlberoException
    highlighter.update_file(
        "test", "def test(): ..."
    )  # Trying to update a file not in the system gives an AlberoException

    tokens: list[Token] = highlighter.get_highlights(
        "test"
    )  # Trying to use a file not in the system gives an AlberoException

    highlighter.remove_file("test")
    highlighter.remove_language(
        "python"
    )  # Can be done first but it will already auto-close any files that use it

    assert tokens == [
        ((1, 0), 3, "Keyword"),
        ((1, 4), 4, "Name"),
        ((1, 8), 3, "Punctuation"),
        ((1, 12), 3, "Operator"),
    ]


def test_mapping_update():
    highlighter = TreeSitterHighlighter()

    highlighter.add_language("python", py_lang, mapping)
    highlighter.update_mapping("python", {})
    highlighter.add_file(
        "test", "python"
    )  # Trying to add a file with a language not in the system gives an AlberoException
    highlighter.update_file(
        "test", "def test(): ..."
    )  # Trying to update a file not in the system gives an AlberoException

    tokens: list[Token] = highlighter.get_highlights(
        "test"
    )  # Trying to use a file not in the system gives an AlberoException
    assert tokens == []


def test_so_file():
    if platform == "darwin":
        assert isinstance(
            lang_from_so("./examples/languages-darwin.so", "python"), Language
        )
