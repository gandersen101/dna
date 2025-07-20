import collections.abc
import typing as ty
from random import randint

from .protocols import CompareableP

Choose = ty.Callable[[collections.abc.Sequence[CompareableP], int, int], int]


def random(
    _s: collections.abc.Sequence[CompareableP], start_idx: int, end_idx: int
) -> int:
    return randint(start_idx, end_idx)


def median_of_3(
    s: collections.abc.Sequence[CompareableP], start_idx: int, end_idx: int
) -> int:
    mid = (start_idx + end_idx) // 2

    if len(s) == 1:
        return 0
    elif len(s) == 2:
        return randint(0, 1)

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
