import collections.abc

import pytest

from dna.protocols import CompareableP
from dna.sort import mergesort

from .params import PARAMS


@pytest.mark.parametrize(*PARAMS)
def test_mergesort(s: collections.abc.Sequence[CompareableP]) -> None:
    assert mergesort(s) == sorted(s)
