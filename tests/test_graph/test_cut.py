import pytest

from dna.graph import cut

from ..loaders import load_adjacency_list


@pytest.mark.flaky(retries=10)
def test_karger_min_cut() -> None:
    assert cut.karger_min(load_adjacency_list()) < 30
    # 17 appears to me the true min cut, but I'm keeping this test looser.
