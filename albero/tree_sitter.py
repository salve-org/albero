from logging import Logger, getLogger

from tree_sitter import Language, Parser, Tree

from .misc import AlberoException, normal_text_range
from .tokens import Token, only_tokens_in_text_range
from .tree_sitter_funcs import edit_tree, node_to_tokens

TreeAndParser = tuple[Tree, Parser, str]  # Tree, Parser, code


class TreeSitterHighlighter:
    """A class that makes highlighting with Tree Sitter significantly easier"""

    def __init__(self) -> None:
        self.languages: dict[str, Language] = {}
        self.files: dict[
            str, tuple[str, TreeAndParser]
        ] = {}  # dict[filename, tuple[language, TreeAndParser]]
        self.mappings: dict[str, dict[str, str]] = {}
        self.logger: Logger = getLogger("TreeSitterHighlighter")
        self.logger.info("Created Highlighter")

    def add_language(
        self, language_name: str, language: Language, mapping: dict[str, str]
    ) -> None:
        self.logger.debug("Adding Language")
        if language_name in self.languages:
            self.logger.exception(
                f"Language {language_name} already an added language"
            )
            raise AlberoException(
                f"Language {language_name} already an added language"
            )

        self.languages[language_name] = language
        self.mappings[language_name] = mapping
        self.logger.info("Added Language")

    def update_mapping(
        self, language_name: str, mapping: dict[str, str]
    ) -> None:
        self.logger.debug("Updating mapping")
        if language_name not in self.languages:
            self.logger.exception(
                f"Language {language_name} not an added language"
            )
            raise AlberoException(
                f"Language {language_name} not an added language"
            )

        self.mappings[language_name] = mapping

    def add_file(self, file_name: str, language_name: str) -> None:
        if language_name not in self.languages:
            self.logger.exception(
                f"Language {language_name} not an added language"
            )
            raise AlberoException(
                f"Language {language_name} not an added language"
            )

        if file_name in self.files:
            self.logger.exception(f"File {file_name} already an added file")
            raise AlberoException(f"File {file_name} already an added file")

        language = self.languages[language_name]
        parser = Parser(language)
        blank_tree: Tree = parser.parse(bytes("", "utf-8"))
        self.files[file_name] = (language_name, (blank_tree, parser, ""))

    def update_file(self, file_name: str, code: str) -> None:
        if file_name not in self.files:
            self.logger.exception(f"File {file_name} not an added file")
            raise AlberoException(f"File {file_name} not an added file")

        old_tree, parser, old_code = self.files[file_name][1]

        new_tree: Tree = edit_tree(old_code, code, old_tree, parser)

        self.files[file_name] = (
            self.files[file_name][0],
            (new_tree, parser, code),
        )

    def get_highlights(
        self, file_name: str, text_range: tuple[int, int] = (1, -1)
    ) -> list[Token]:
        if file_name not in self.files:
            self.logger.exception(f"File {file_name} not an added file")
            raise AlberoException(f"File {file_name} not an added file")

        return_tokens: list[Token]

        tree, parser, code = self.files[file_name][1]

        split_text, text_range = normal_text_range(code, text_range)

        return_tokens = node_to_tokens(
            tree, self.mappings[self.files[file_name][0]], self.logger
        )
        return_tokens = only_tokens_in_text_range(return_tokens, text_range)
        return return_tokens

    def remove_file(self, file_name: str) -> None:
        if file_name not in self.files:
            self.logger.exception(f"File {file_name} not an added file")
            raise AlberoException(f"File {file_name} not an added file")

        self.files.pop(file_name)

    def remove_language(self, language_name: str) -> None:
        if language_name not in self.languages:
            self.logger.exception(
                f"Language {language_name} not an added language"
            )
            raise AlberoException(
                f"Language {language_name} not an added language"
            )

        self.languages.pop(language_name)

        files: dict[str, tuple[str, TreeAndParser]] = {}
        for file in self.files:
            if self.files[file][0] == language_name:
                continue

            files[file] = self.files[file]

        self.files = files
