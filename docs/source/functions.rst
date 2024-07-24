=========
Functions
=========

.. _lang_from_so Overview:

``lang_from_so(path: str | pathlib.Path, name: str) -> tree_sitter.Language``
*****************************************************************************

This function takes a ``.so`` file and the language name (used by the old tree sitter versions) and returns a ``tree_sitter.Language`` for usage with Albero.

.. _get_lang Overview:

``get_lang(language_name: str) -> tree_sitter.Language``
********************************************************

Takes a language name and attempts to get a ``tree_sitter.Language`` from the dict of builtin Tree Sitter languages.

.. _get_mapping Overview:

``get_mapping(language_name: str) -> dict[str, str]``
*****************************************************

Takes a language name and attempts to get a mapping from the dict of pre-made mappings.
