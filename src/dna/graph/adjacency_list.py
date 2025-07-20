import collections.abc
import typing as ty

from .node import NodeP

N = ty.TypeVar("N", bound=NodeP)

AdjacencyListMapping = collections.abc.Mapping[N, collections.abc.Sequence[N]]


def mutable_alm_copy(
    adjacency_list_mapping: AdjacencyListMapping[N],
) -> dict[N, list[N]]:
    return {k: list(v) for k, v in adjacency_list_mapping.items()}
