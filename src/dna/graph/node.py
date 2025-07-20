import abc
import collections.abc
import typing as ty


class NodeP(collections.abc.Hashable, ty.Protocol):
    @abc.abstractmethod
    def __eq__(self, other: ty.Any) -> bool:
        return NotImplemented
