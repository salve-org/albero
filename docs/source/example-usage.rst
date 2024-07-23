=============
Example Usage
=============

Now that you have ``Albero`` installed, let's try running a simple example that prints out the highlight ``Token``'s of the file being run:

.. code-block:: python

    from tree_sitter import Language

    from albero import Token, TreeSitterHighlighter, get_lang, get_mapping

    py_lang: Language = get_lang("python")
    mapping: dict[str, str] = get_mapping("python")


    highlighter = TreeSitterHighlighter()

    highlighter.add_language("python", py_lang, mapping)
    highlighter.add_file(
    "test", "python"
    )  # Trying to add a file with a language not in the system gives an Exception
    highlighter.update_file(
    "test", "def test(): ..."
    )  # Trying to update a file not in the system gives an Exception

    tokens: list[Token] = highlighter.get_highlights(
    "test"
    )  # Trying to use a file not in the system gives an Exception

    highlighter.remove_file("test")
    highlighter.remove_language(
    "python"
    )  # Can be done first but it will already auto-close any files that use it

    print(tokens)

.. |br| raw:: html

   <br />

|br|
