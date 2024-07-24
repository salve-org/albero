from beartype.typing import Callable
from tree_sitter import Language

from .bash import bash_language
from .c import c_language
from .c_sharp import c_sharp_language
from .commonlisp import commonlisp_language
from .cpp import cpp_language
from .css import css_language
from .cuda import cuda_language
from .embedded_template import embedded_template_language
from .glsl import glsl_language
from .go import go_language
from .gstlaunch import gstlaunch_language
from .html import html_language
from .java import java_language, java_mapping
from .javascript import javascript_language
from .jsdoc import jsdoc_language
from .json import json_language
from .odin import odin_language
from .php import php_language
from .pymanifest import pymanifest_language
from .python import python_language, python_mapping
from .ruby import ruby_language
from .rust import rust_language
from .scss import scss_language
from .slang import slang_language
from .starlark import starlark_language
from .toml import toml_language
from .typescript import typescript_language
from .wgsl_bevy import wgsl_bevy_language
from .yaml import yaml_language

# from .arduino import arduino_language

language_functions: dict[str, Callable] = {
    "starlark": starlark_language,
    "commonlisp": commonlisp_language,
    "odin": odin_language,
    "glsl": glsl_language,
    "javascript": javascript_language,
    "python": python_language,
    "toml": toml_language,
    "bash": bash_language,
    "c_sharp": c_sharp_language,
    "c": c_language,
    "php": php_language,
    "cuda": cuda_language,
    "pymanifest": pymanifest_language,
    # "arduino": arduino_language,
    "css": css_language,
    "embedded_template": embedded_template_language,
    "jsdoc": jsdoc_language,
    "wgsl_bevy": wgsl_bevy_language,
    "html": html_language,
    "yaml": yaml_language,
    "cpp": cpp_language,
    "slang": slang_language,
    "ruby": ruby_language,
    "java": java_language,
    "scss": scss_language,
    "go": go_language,
    "json": json_language,
    "rust": rust_language,
    "typescript": typescript_language,
    "gstlaunch": gstlaunch_language,
}
language_mappings: dict[str, dict[str, str]] = {
    "python": python_mapping,
    "java": java_mapping,
}


def get_lang(language_name: str) -> Language:
    if language_name not in language_functions:
        raise Exception("Language not in pre-compiled languages")

    return Language(language_functions[language_name]())


def get_mapping(language_name: str) -> dict[str, str]:
    if language_name not in language_mappings:
        raise Exception("Language not in pre-compiled mappings")

    return language_mappings[language_name]
