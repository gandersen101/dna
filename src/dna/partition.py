import collections.abc

from .types import CompareableT


def partition(
    s: collections.abc.MutableSequence[CompareableT], start_idx: int, end_idx: int
) -> int:
    pivot_value = s[start_idx]
    pivot_boundary = start_idx + 1

    for elements_processed in range(start_idx + 1, end_idx + 1):
        if s[elements_processed] < pivot_value:
            s[elements_processed], s[pivot_boundary] = (
                s[pivot_boundary],
                s[elements_processed],
            )
            pivot_boundary += 1

    partition_idx = pivot_boundary - 1

    s[start_idx], s[partition_idx] = s[partition_idx], s[start_idx]

    partition.n_comparisons = len(s[start_idx:end_idx])  # type: ignore[attr-defined]

    return partition_idx
