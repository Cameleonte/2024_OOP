class IDMixin:
    ID: int = 1

    @classmethod
    def get_next_id(cls) -> int:
        return cls.ID

    @classmethod
    def increment_id(cls) -> None:
        cls.ID += 1
