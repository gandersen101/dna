import typing as ty

import pytest

from dna.sort import quicksort
from dna.sort.quicksort import ChoosePivot, _median_of_3
from dna.types import CompareableT

from ..loaders import load_10_unique_ints2, load_10k_unique_ints, load_100_unique_ints
from .params import PARAMS


@pytest.mark.parametrize(*PARAMS)
def test_quicksort(s: ty.MutableSequence[CompareableT]) -> None:
    s_list = list(s)
    expected = sorted(s)

    assert quicksort(s_list) == expected
    assert s_list == expected  # quicksort sorts in-place


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
            _median_of_3,
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
            _median_of_3,
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
            _median_of_3,
            138_382,
            id="choose median pivot - 10k unique ints",
        ),
    ],
)
def test_quicksort_comparison_counts(
    s: ty.MutableSequence[CompareableT],
    choose_pivot: ChoosePivot,
    n_comparisons: int,
) -> None:
    quicksort(list(s), choose_pivot=choose_pivot)
    assert quicksort.n_comparisons == n_comparisons  # type: ignore[attr-defined]
