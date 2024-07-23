from ctypes import c_void_p, cdll
from os import fspath

from tree_sitter import Language


def normal_text_range(
    full_text: str, text_range: tuple[int, int] = (1, -1)
) -> tuple[list[str], tuple[int, int]]:
    split_text: list[str] = full_text.splitlines()

    if text_range[1] == -1:
        # This indicates that the text range should span the length of the entire code
        text_range = (text_range[0], len(split_text))

    # We want only the lines in the text range because this list is iterated
    split_text = split_text[text_range[0] - 1 : text_range[1]]

    return (split_text, text_range)


def lang_from_so(path: str, name: str) -> Language:
    lib = cdll.LoadLibrary(fspath(path))
    language_function = getattr(lib, f"tree_sitter_{name}")
    language_function.restype = c_void_p
    language_ptr = language_function()
    return Language(language_ptr)


class AlberoException(Exception): ...  # I don't like the boilerplate either
