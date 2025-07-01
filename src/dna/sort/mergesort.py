import typing as ty

from ..types import CompareableT


def _merge(
    s1: ty.Sequence[CompareableT], s2: ty.Sequence[CompareableT]
) -> list[CompareableT]:
    len_s1 = len(s1)
    len_s2 = len(s2)

    i_s1 = 0
    i_s2 = 0

    result = []

    while i_s1 < len_s1 and i_s2 < len_s2:
        # consume at least one of the subarrays
        if s1[i_s1] < s2[i_s2]:
            result.append(s1[i_s1])
            i_s1 += 1
        else:
            result.append(s2[i_s2])
            i_s2 += 1

    if i_s1 < len_s1:
        result.extend(s1[i_s1:])
    elif i_s2 < len_s2:
        result.extend(s2[i_s2:])
    # extend result with any remaining values from potentially unconsummed array

    return result


def mergesort(s: ty.Sequence[CompareableT]) -> list[CompareableT]:
    len_s = len(s)

    if len_s <= 1:  # base case
        return list(s)

    middle = len_s // 2

    left = mergesort(s[:middle])
    right = mergesort(s[middle:])
    # recursion

    return _merge(left, right)  # combine
