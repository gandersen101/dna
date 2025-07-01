import typing as ty

from ..types import CompareableT

ChoosePivot = ty.Callable[[ty.MutableSequence[CompareableT], int, int], int]


def _median_of_3(
    s: ty.MutableSequence[CompareableT], start_idx: int, end_idx: int
) -> int:
    mid = (start_idx + end_idx) // 2

    if s[start_idx] > s[mid]:
        if s[start_idx] < s[end_idx]:
            return start_idx
        elif s[mid] > s[end_idx]:
            return mid
        else:
            return end_idx

    if s[start_idx] > s[end_idx]:
        return start_idx
    elif s[mid] < s[end_idx]:
        return mid
    else:
        return end_idx


def _partition(
    s: ty.MutableSequence[CompareableT], start_idx: int, end_idx: int
) -> tuple[int, int]:
    pivot_value = s[start_idx]
    pivot_boundary = start_idx + 1

    for elements_processed in range(start_idx + 1, end_idx + 1):
        if s[elements_processed] < pivot_value:
            s[elements_processed], s[pivot_boundary] = (
                s[pivot_boundary],
                s[elements_processed],
            )
            pivot_boundary += 1

    s[start_idx], s[pivot_boundary - 1] = s[pivot_boundary - 1], s[start_idx]

    return pivot_boundary - 1, len(s[start_idx:end_idx])


def quicksort(
    s: ty.MutableSequence[CompareableT], *, choose_pivot: ChoosePivot = _median_of_3
) -> ty.MutableSequence[CompareableT]:
    start_idx = 0
    end_idx = len(s) - 1

    def _quicksort(
        s: ty.MutableSequence[CompareableT], start_idx: int, end_idx: int
    ) -> tuple[ty.MutableSequence[CompareableT], int]:
        if start_idx >= end_idx:  # base case
            return s, 0

        pivot_idx = choose_pivot(s, start_idx, end_idx)
        s[start_idx], s[pivot_idx] = s[pivot_idx], s[start_idx]

        partition_idx, comparisons = _partition(s, start_idx, end_idx)

        _, left_comparisons = _quicksort(s, start_idx, partition_idx - 1)
        _, right_comparisons = _quicksort(s, partition_idx + 1, end_idx)
        # recursion

        return s, left_comparisons + right_comparisons + comparisons

    s, comparisons = _quicksort(s, start_idx, end_idx)
    quicksort.n_comparisons = comparisons  # type: ignore[attr-defined]

    return s
