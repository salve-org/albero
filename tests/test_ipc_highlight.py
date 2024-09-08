from time import sleep

from beartype.typing import Callable

from albero import IPCHighlighter, Token, get_lang_func, get_mapping

py_lang: Callable = get_lang_func("python")
mapping: dict[str, str] = get_mapping("python")


def test_basic_usage():
    highlighter = IPCHighlighter()

    highlighter.add_language("python", py_lang, mapping)
    highlighter.add_file("test", "python")
    highlighter.update_file("test", "def test(): ...")
    highlighter.request_highlights(
        "test"
    )  # Trying to use a file not in the system gives an AlberoException
    highlighter.remove_file("test")
    sleep(1)
    tokens: list[Token] | None = highlighter.get_highlight_response()

    assert tokens == [
        ((1, 0), 3, "Keyword"),
        ((1, 4), 4, "Identifier"),
        ((1, 8), 3, "Punctuation"),
        ((1, 12), 3, "Operator"),
    ]
