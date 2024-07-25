class foo:
    def bar() -> None:
        if baz:  # noqa: F821
            qux()  # noqa: F821
