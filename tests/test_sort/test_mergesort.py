import typing as ty

import pytest

from dna.sort import mergesort
from dna.types import CompareableT

from .params import PARAMS


@pytest.mark.parametrize(*PARAMS)
def test_mergesort(s: ty.Sequence[CompareableT]) -> None:
    assert mergesort(s) == sorted(s)
