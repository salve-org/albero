=========
Variables
=========

.. _Token Overview:

``Token``
*********

The ``Token`` type is, in reality, just a type alias of ``tuple[tuple[int, int], int, str]``. Despite simply being a ``tuple``, the ``Token`` is the most frequently returned data type. That being said, what data does it signify?

The ``Token`` type contains three parts: the start index, its length, and its type. The start index is that ``tuple`` at the beginning of the main ``tuple`` and the first index of that is the line the ``Token`` takes place on and the second is the column. ``Token``'s start at index ``1, 0`` so you may need to do a -1 or a +1 depending on how you need to use this data. The second ``int`` is the length of the ``Token`  and the ``str`` is the type. You will use these very often so its never a bad idea to get  familiar with them.

.. _Generic Tokens Overview:

``generic_tokens``
******************

The ``GENERIC_TOKENS`` ``list`` provides all the generic ``Token`` types you will encounter when using ``Albero``. Simply print this out and you will know all possible ``Token`` types and will never be surprised by a random ``Token`` type again.
