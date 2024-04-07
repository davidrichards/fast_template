class BodyInitializationError(ValueError):
    pass


class Body(str):
    def __new__(cls, value: str):
        if isinstance(value, cls):
            return value

        if not value:
            raise BodyInitializationError("Body cannot be empty")
        if not value.strip():
            raise BodyInitializationError("Body cannot be whitespace")
        if len(value) > 1024 * 1024 * 1024:
            raise BodyInitializationError("Body cannot be longer than 1GB")
        return str.__new__(cls, value)


class TitleInitializationError(ValueError):
    pass


class Title(str):
    def __new__(cls, value: str):
        if isinstance(value, cls):
            return value

        if not value:
            raise TitleInitializationError("Title cannot be empty")
        if not value.strip():
            raise TitleInitializationError("Title cannot be whitespace")
        if len(value) > 1024:
            raise TitleInitializationError("Title cannot be longer than 1KB")
        return str.__new__(cls, value)


__all__ = ["Body", "Title"]
