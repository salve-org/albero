# pip install -U -r requirements-dev.txt --break-system-packages; pip uninstall albero -y --break-system-packages; pip install . --break-system-packages --no-build-isolation; python3 -m pytest .
from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()


setup(
    name="albero",
    version="0.0.1",
    description="Albero is a tool that makes it much easier to use Tree Sitter for your code editors",
    author="Moosems",
    author_email="moosems.j@gmail.com",
    url="https://github.com/Moosems/albero",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["beartype", "tree-sitter"],
    python_requires=">=3.11",
    license="MIT license",
    classifiers=[
        # "Development Status :: 3 - Beta",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Typing :: Typed",
    ],
    packages=["albero", "albero.languages"],
)
