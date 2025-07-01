import pytest
from _pytest.mark.structures import ParameterSet

from dna.math.multiply import grade_school_int_mult, karatsuba_int_mult

INT_MULT_PARAMS: tuple[tuple[str, str], tuple[ParameterSet, ...]] = (
    ("int1", "int2"),
    (
        pytest.param(4, 5, id="single digits"),
        pytest.param(1234, 5678, id="powers of two"),
        pytest.param(12345, 67890, id="not powers of two"),
        pytest.param(1234, 56789, id="mixed powers"),
        pytest.param(
            3141592653589793238462643383279502884197169399375105820974944592,
            2718281828459045235360287471352662497757247093699959574966967627,
            id="algorithms illuminated 1.6",
        ),
    ),
)


@pytest.mark.parametrize(*INT_MULT_PARAMS)
def test_grade_school_int_mult(int1: int, int2: int) -> None:
    assert grade_school_int_mult(int1, int2) == int1 * int2


@pytest.mark.parametrize(*INT_MULT_PARAMS)
def test_karatsuba_int_mult(int1: int, int2: int) -> None:
    assert karatsuba_int_mult(int1, int2) == int1 * int2
