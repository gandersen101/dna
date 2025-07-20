import collections.abc

import pytest

from dna.inversions import count_inversions
from dna.protocols import CompareableP

from .loaders import load_10_unique_ints1, load_100k_unique_ints


@pytest.mark.parametrize(
    ["s", "inversions"],
    [
        pytest.param(load_10_unique_ints1(), 28, id="10 unique ints"),
        pytest.param(load_100k_unique_ints(), 2_407_905_288, id="100k unique ints"),
        pytest.param(["a", "b", "c", "d"], 0, id="string array with no inversions"),
    ],
)
def test_count_inversions(
    s: collections.abc.Sequence[CompareableP], inversions: int
) -> None:
    assert count_inversions(s) == inversions
