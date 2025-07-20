import collections.abc
import typing as ty
from functools import lru_cache
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"

T = ty.TypeVar("T")


@lru_cache(None)
def _load_newline_delimited_file_as_tuple(type_: type[T], path: Path) -> tuple[T, ...]:
    return tuple([type_(line) for line in open(path).readlines()])  # type: ignore[call-arg]


def load_10_unique_ints1() -> tuple[int, ...]:
    return _load_newline_delimited_file_as_tuple(int, DATA_PATH / "10_unique_ints1.txt")


def load_10_unique_ints2() -> tuple[int, ...]:
    return _load_newline_delimited_file_as_tuple(int, DATA_PATH / "10_unique_ints2.txt")


def load_100_unique_ints() -> tuple[int, ...]:
    return _load_newline_delimited_file_as_tuple(int, DATA_PATH / "100_unique_ints.txt")


def load_10k_unique_ints() -> tuple[int, ...]:
    return _load_newline_delimited_file_as_tuple(int, DATA_PATH / "10k_unique_ints.txt")


def load_100k_unique_ints() -> tuple[int, ...]:
    return _load_newline_delimited_file_as_tuple(
        int, DATA_PATH / "100k_unique_ints.txt"
    )


def load_adjacency_list() -> collections.abc.Mapping[int, tuple[int, ...]]:
    graph = {}

    with open(DATA_PATH / "karger_min_cut.txt") as f:
        for ln in f:
            line = ln.split()
            if line:
                vertices = tuple([int(x) for x in line[1:]])
                graph[int(line[0])] = vertices

    return graph
