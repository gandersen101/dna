import pytest
from _pytest.mark.structures import ParameterSet

from ..loaders import (
    load_10_unique_ints1,
    load_10_unique_ints2,
    load_10k_unique_ints,
    load_100_unique_ints,
    load_100k_unique_ints,
)

PARAMS: tuple[str, tuple[ParameterSet, ...]] = (
    "s",
    (
        pytest.param([5, 3, 4, 1, 6, 2], id="even length integer array"),
        pytest.param(["z", "b", "c", "w", "y"], id="even length string array"),
        pytest.param([5, 3, 4, 1, 6], id="uneven int array"),
        pytest.param([5, 5, 3, 3, 6, 1, 1], id="uneven int array with duplicates"),
        pytest.param(load_10_unique_ints1(), id="10 unique ints - 1"),
        pytest.param(load_10_unique_ints2(), id="10 unique ints - 2"),
        pytest.param(load_100_unique_ints(), id="100 unique ints"),
        pytest.param(load_10k_unique_ints(), id="10k unique ints"),
        pytest.param(load_100k_unique_ints(), id="100k unique ints"),
    ),
)
