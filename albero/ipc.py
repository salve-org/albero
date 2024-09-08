from pathlib import Path

from beartype.typing import Callable
from collegamento import (
    USER_FUNCTION,
    Client,
    Request,
    RequestQueueType,
    Response,
    ResponseQueueType,
    Server,
)
from token_tools import Token
from tree_sitter import Language

from .misc import AlberoException, lang_from_so
from .tree_sitter import TreeSitterHighlighter


def add_language(server: "IPCHighlightServer", request: Request) -> None:
    language: str | Path | Callable = request["language"]  # type: ignore
    lang_name: str = request["language_name"]  # type: ignore
    lang: Language
    if isinstance(language, Callable):
        lang = Language(language())
    elif isinstance(language, str):
        lang = lang_from_so(language, lang_name)
    else:
        lang = lang_from_so(str(language), lang_name)
    server.highlighter.add_language(lang_name, lang, request["mapping"])  # type: ignore


def remove_language(server: "IPCHighlightServer", request: Request) -> None:
    server.highlighter.remove_language(request["language_name"])  # type: ignore


def add_file(server: "IPCHighlightServer", request: Request) -> None:
    server.highlighter.add_file(request["file_name"], request["language_name"])  # type: ignore


def update_file(server: "IPCHighlightServer", request: Request) -> None:
    server.highlighter.update_file(request["file_name"], request["code"])  # type: ignore


def remove_file(server: "IPCHighlightServer", request: Request) -> None:
    server.highlighter.remove_file(request["file_name"])  # type: ignore


def update_mapping(server: "IPCHighlightServer", request: Request) -> None:
    server.highlighter.update_mapping(
        request["language_name"],  # type: ignore
        request["mapping"],  # type: ignore
    )


def get_highlights(
    server: "IPCHighlightServer", request: Request
) -> list[Token]:
    return server.highlighter.get_highlights(
        request["file_name"],  # type: ignore
        request["text_range"],  # type: ignore
    )


class IPCHighlighter(Client):
    def __init__(self, id_max: int = 15000) -> None:
        self.faux_langs: list[str] = []
        self.faux_files: dict[str, str] = {}  # file, lang
        commands: dict[str, USER_FUNCTION] = {
            "add-language": add_language,
            "remove-language": remove_language,
            "add-file": add_file,
            "update-file": update_file,
            "remove-file": remove_file,
            "update-mapping": update_mapping,
            "get-highlights": get_highlights,
        }
        super().__init__(commands, id_max, server_type=IPCHighlightServer)  # type: ignore

    def get_response(self) -> Response | None:  # type: ignore
        return super().get_response("get-highlights")  # type: ignore

    def add_language(
        self,
        language_name: str,
        language: Callable | Path | str,
        mapping: dict[str, str],
    ) -> None:
        if language_name in self.faux_langs:
            raise AlberoException(
                f"Language {language_name} already an added language"
            )

        self.faux_langs.append(language_name)
        super().request(
            "add-language",
            language_name=language_name,
            language=language,
            mapping=mapping,
        )

    def remove_language(self, language_name: str) -> None:
        if language_name not in self.faux_langs:
            raise AlberoException(
                f"Language {language_name} not an added language"
            )

        self.faux_langs.remove(language_name)

        new_faux_files: dict[str, str] = {}
        for file, lang in self.faux_files:
            if lang == language_name:
                continue

            new_faux_files[file] = lang

        self.faux_files = new_faux_files

    def add_file(self, file_name: str, language_name: str) -> None:
        if language_name not in self.faux_langs:
            raise AlberoException(
                f"Language {language_name} not an added language"
            )

        if file_name in self.faux_files:
            raise AlberoException(f"File {file_name} already an added file")

        self.faux_files[file_name] = language_name
        super().request(
            "add-file", file_name=file_name, language_name=language_name
        )

    def update_file(self, file_name: str, code: str) -> None:
        if file_name not in self.faux_files:
            raise AlberoException(f"File {file_name} not an added file")

        super().request("update-file", file_name=file_name, code=code)

    def remove_file(self, file_name: str) -> None:
        if file_name not in self.faux_files:
            raise AlberoException(f"File {file_name} not an added file")

        self.faux_files.pop(file_name)
        super().request("remove-file", file_name=file_name)

    def update_mapping(
        self, language_name: str, mapping: dict[str, str]
    ) -> None:
        if language_name not in self.faux_langs:
            raise AlberoException(
                f"Language {language_name} not an added language"
            )

        super().request(
            "update-mapping", language_name=language_name, mapping=mapping
        )

    def request_highlights(
        self, file_name: str, text_range: tuple[int, int] = (1, -1)
    ) -> None:
        if file_name not in self.faux_files:
            raise AlberoException(f"File {file_name} not an added file")

        super().request(
            "get-highlights", file_name=file_name, text_range=text_range
        )

    def get_highlight_response(self) -> list[Token] | None:  # type: ignore
        response = super().get_response("get-highlights")

        if response is not None:
            return response["result"]  # type: ignore

        return None


class IPCHighlightServer(Server):
    def __init__(
        self,
        commands: dict[str, tuple[USER_FUNCTION, bool]],
        response_queue: ResponseQueueType,
        requests_queue: RequestQueueType,
    ) -> None:
        self.highlighter = TreeSitterHighlighter()
        super().__init__(
            commands,
            response_queue,  # type: ignore
            requests_queue,  # type: ignore
            [
                "add-language",
                "update-mapping",
                "add-file",
                "update-file",
                "get-highlights",
                "remove-file",
                "remove-language",
            ],
        )
