import collections.abc

from .types import CompareableT


def _merge_and_count_split_inversions(
    s1: collections.abc.Sequence[CompareableT],
    s2: collections.abc.Sequence[CompareableT],
) -> tuple[list[CompareableT], int]:
    len_s1 = len(s1)
    len_s2 = len(s2)

    i_s1 = 0
    i_s2 = 0

    sorted_lst = []
    split_invs = 0

    while i_s1 < len_s1 and i_s2 < len_s2:
        if s1[i_s1] < s2[i_s2]:
            sorted_lst.append(s1[i_s1])
            i_s1 += 1
        else:
            sorted_lst.append(s2[i_s2])
            split_invs += len_s1 - i_s1
            i_s2 += 1

    if i_s1 < len_s1:
        sorted_lst.extend(s1[i_s1:])
    elif i_s2 < len_s2:
        sorted_lst.extend(s2[i_s2:])
    # extend result with any remaining values from potentially unconsummed array

    return sorted_lst, split_invs


def _mergesort_and_count_inversions(
    s: collections.abc.Sequence[CompareableT],
) -> tuple[list[CompareableT], int]:
    len_s = len(s)

    if len_s <= 1:  # base case
        return list(s), 0

    middle = len_s // 2

    left, left_invs = _mergesort_and_count_inversions(s[:middle])
    right, right_invs = _mergesort_and_count_inversions(s[middle:])
    # recursion

    sorted_lst, split_invs = _merge_and_count_split_inversions(left, right)  # combine

    return sorted_lst, left_invs + right_invs + split_invs


def count_inversions(s: collections.abc.Sequence[CompareableT]) -> int:
    return _mergesort_and_count_inversions(s)[1]
