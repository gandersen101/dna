import collections.abc

import pytest

from dna.protocols import CompareableP
from dna.select import rselect

from .loaders import (
    load_10_unique_ints1,
    load_10_unique_ints2,
    load_10k_unique_ints,
    load_100_unique_ints,
    load_100k_unique_ints,
)


@pytest.mark.parametrize(
    ["s", "order_statistic"],
    [
        pytest.param(load_10_unique_ints1(), 3, id="10 unique ints - 1"),
        pytest.param(load_10_unique_ints2(), 7, id="10 unique ints - 2"),
        pytest.param(load_100_unique_ints(), 44, id="100 unique ints"),
        pytest.param(load_10k_unique_ints(), 2112, id="10k unique ints"),
        pytest.param(load_100k_unique_ints(), 87_941, id="100k unique ints"),
    ],
)
def test_mergesort(
    s: collections.abc.Sequence[CompareableP], order_statistic: int
) -> None:
    assert rselect(s, order_statistic) == sorted(s)[order_statistic - 1]
