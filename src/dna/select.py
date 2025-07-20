import collections.abc

from . import pivot
from .partition import partition
from .protocols import CompareableP


def rselect(
    s: collections.abc.Sequence[CompareableP],
    order_statistic: int,
    *,
    choose_pivot: pivot.Choose = pivot.median_of_3,
) -> CompareableP:
    if order_statistic <= 0:
        raise ValueError(
            f"Cannot have an order statistic less than 1. Got {order_statistic}."
        )
    elif order_statistic > len(s):
        raise ValueError(
            f"Cannot have an order statistic greater than length of `s`. Got {order_statistic}."
        )

    order_statistic -= 1

    def _rselect(
        s: collections.abc.MutableSequence[CompareableP], order_statistic: int
    ) -> CompareableP:
        n = len(s)
        start_idx = 0
        end_idx = n - 1

        if n == 1:  # base case
            return s[0]

        pivot_idx = choose_pivot(s, start_idx, end_idx)
        s[start_idx], s[pivot_idx] = s[pivot_idx], s[start_idx]

        partition_idx = partition(s, start_idx, end_idx)

        if partition_idx == order_statistic:
            return s[partition_idx]  # lucky
        elif partition_idx > order_statistic:
            return _rselect(s[:partition_idx], order_statistic)  # recursion

        return _rselect(s[partition_idx:], order_statistic - partition_idx)  # recursion

    return _rselect(list(s), order_statistic)
