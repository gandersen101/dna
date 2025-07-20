import collections.abc

import pytest

from dna import pivot
from dna.sort import quicksort

from ..loaders import load_10_unique_ints2, load_10k_unique_ints, load_100_unique_ints
from .params import PARAMS


@pytest.mark.parametrize(*PARAMS)
def test_quicksort(s: collections.abc.Sequence[int]) -> None:
    expected = sorted(s)

    assert quicksort(list(s)) == expected


@pytest.mark.parametrize(
    ["s", "choose_pivot", "n_comparisons"],
    [
        pytest.param(
            load_10_unique_ints2(),
            lambda x, y, z: y,
            25,
            id="choose first pivot - 10 unique ints",
        ),
        pytest.param(
            load_10_unique_ints2(),
            lambda x, y, z: z,
            31,
            id="choose last pivot - 10 unique ints",
        ),
        pytest.param(
            load_10_unique_ints2(),
            pivot.median_of_3,
            21,
            id="choose median pivot - 10 unique ints",
        ),
        pytest.param(
            load_100_unique_ints(),
            lambda x, y, z: y,
            620,
            id="choose first pivot - 100 unique ints",
        ),
        pytest.param(
            load_100_unique_ints(),
            lambda x, y, z: z,
            573,
            id="choose last pivot - 100 unique ints",
        ),
        pytest.param(
            load_100_unique_ints(),
            pivot.median_of_3,
            502,
            id="choose median pivot - 100 unique ints",
        ),
        pytest.param(
            load_10k_unique_ints(),
            lambda x, y, z: y,
            162_085,
            id="choose first pivot - 10k unique ints",
        ),
        pytest.param(
            load_10k_unique_ints(),
            lambda x, y, z: z,
            164_123,
            id="choose last pivot - 10k unique ints",
        ),
        pytest.param(
            load_10k_unique_ints(),
            pivot.median_of_3,
            138_382,
            id="choose median pivot - 10k unique ints",
        ),
    ],
)
def test_quicksort_w_ints_comparison_counts(
    s: collections.abc.Sequence[int],
    choose_pivot: pivot.Choose,
    n_comparisons: int,
) -> None:
    quicksort(list(s), choose_pivot=choose_pivot)
    assert quicksort.n_comparisons == n_comparisons  # type: ignore[attr-defined]
