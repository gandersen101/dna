import collections.abc

import pytest

from dna.sort import mergesort

from .params import PARAMS


@pytest.mark.parametrize(*PARAMS)
def test_mergesort(s: collections.abc.Sequence[int]) -> None:
    assert mergesort(s) == sorted(s)
