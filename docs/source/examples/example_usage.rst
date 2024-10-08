=============
Example Usage
=============

.. code-block:: python

    from logging import INFO, Logger, basicConfig, getLogger
    
    from tree_sitter import Language
    
    from albero import Token, TreeSitterHighlighter, get_lang, get_mapping
    
    basicConfig(
        level=INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logger: Logger = getLogger("Main")
    
    py_lang: Language = get_lang("python")
    mapping: dict[str, str] = get_mapping("python")
    
    
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
    
    print(tokens)

See the file example file `here <https://github.com/Moosems/albero/blob/master/examples/example_usage.py>`_.