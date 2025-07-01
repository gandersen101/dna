import typing as ty


class CompareableP(ty.Protocol):
    def __lt__(self, other: ty.Any) -> bool: ...
