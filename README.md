<h1 align="center">Albero v0.0.2</h1>

A tool that makes it much easier to use Tree Sitter for your code editors

# Installation

In the Command Line, paste the following: `pip install albero`

## Description

Albero is a library that can be used by code editors to easily get syntax highlighting from tree-sitter. It simplifies the process of getting readily usable tokens and only requires a `Language` or `.so` language file along with the languages mapping to get started (some are pre-included with the module). Docs are listed on this [ReadTheDocs page](https://albero.readthedocs.io/en/master/)

> **Notes:**
>  - This project is super early on and will probably be moved to `salve-org` shortly. This originally was created for the main tool `Salve` but that may or may not be split into multiple tools dor simplicity's sake.

## Contributing

To contribute, fork the repository, make your changes, and then make a pull request. If you want to add a feature, please open an issue first so it can be discussed. Note that whenever and wherever possible you should try to use stdlib modules rather than external ones.

## Required Python Version: 3.11+

Albero will use the three most recent versions (full releases) going forward and will drop any older versions as new ones come out. This is because I hope to keep this package up to date with modern python versions as they come out instead of being forced to maintain decade old python versions.
Currently 3.11 is the minimum (instead of 3.10) as this was developed under 3.12 and there are many features that it relies on from this version I want. However, after 3.14 is released, the minimum version will be 3.12 (as would be expected from the plan) and will change accordingly in the future as is described in the plan above.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE).
