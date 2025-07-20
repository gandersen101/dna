import collections.abc

from .. import pivot
from ..partition import partition
from ..protocols import CompareableP


def quicksort(
    s: collections.abc.MutableSequence[CompareableP],
    *,
    choose_pivot: pivot.Choose = pivot.median_of_3,
) -> collections.abc.MutableSequence[CompareableP]:
    start_idx = 0
    end_idx = len(s) - 1

    def _quicksort(
        s: collections.abc.MutableSequence[CompareableP], start_idx: int, end_idx: int
    ) -> tuple[collections.abc.MutableSequence[CompareableP], int]:
        if start_idx >= end_idx:  # base case
            return s, 0

        pivot_idx = choose_pivot(s, start_idx, end_idx)
        s[start_idx], s[pivot_idx] = s[pivot_idx], s[start_idx]

        partition_idx = partition(s, start_idx, end_idx)
        comparisons = partition.n_comparisons  # type: ignore[attr-defined]
        partition.n_comparisons = 0  # type: ignore[attr-defined]

        _, left_comparisons = _quicksort(s, start_idx, partition_idx - 1)
        _, right_comparisons = _quicksort(s, partition_idx + 1, end_idx)
        # recursion

        return s, left_comparisons + right_comparisons + comparisons

    s, comparisons = _quicksort(s, start_idx, end_idx)
    quicksort.n_comparisons = comparisons  # type: ignore[attr-defined]

    return s
