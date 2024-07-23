from beartype.claw import beartype_this_package

beartype_this_package()

from .languages import get_lang, get_mapping  # noqa: F401
from .tokens import Token  # noqa: F401
from .tree_sitter import TreeSitterHighlighter  # noqa: F401
