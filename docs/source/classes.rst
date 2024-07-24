=======
Classes
=======

.. _TreeSitterHighlighter Overview:

``TreeSitterHighlighter``
*************************

The ``TreeSitterHighlighter`` is a class that provides the following methods for usage:

- ``TreeSitterHighlighter.add_language(self, language_name: str, language: Language, mapping: dict[str, str]) -> None``
- ``TreeSitterHighlighter.update_mapping(self, language_name: str, mapping: dict[str, str]) -> None``
- ``TreeSitterHighlighter.add_file(self, file_name: str, language_name: str) -> None``
- ``TreeSitterHighlighter.update_file(self, file_name: str, code: str) -> None``
- ``TreeSitterHighlighter.get_highlights(self, file_name: str, text_range: tuple[int, int] = (1, -1)) -> list[Token]`` (text range is inclusive of lines given and a -1 in the second position marks to go till the end of the file
- ``TreeSitterHighlighter.remove_file(self, file_name: str) -> None``
- ``TreeSitterHighlighter.remove_language(self, language_name: str) -> None``

.. _AlberoException Overview:

``AlberoException``
*******************

The ``AlberoException`` class is a simple ``Exception`` subclass for ``Albero``
