def _val_int_mult_inputs(int1: int, int2: int) -> None:
    if int1 < 0 or int2 < 0:
        raise ValueError(
            "This integer multiplication implementation does not support negative integers."
        )


def _prep_int_mult_inputs(int1: str, int2: str) -> tuple[str, str]:
    n = max(len(int1), len(int2))

    while (n & (n - 1)) != 0:  # find closest power of 2 for largest input
        n += 1

    def pad(int_str: str) -> str:
        return "0" * max(n - len(int_str), 0) + int_str

    return pad(int1), pad(int2)


def _grade_school_int_mult(int1: str, int2: str) -> int:
    x_len = len(int1)
    y_len = len(int2)
    assert x_len == y_len, "int1 and int2 must have the same length - n"
    n = x_len  # convenience

    if n == 1:  # base case
        return int(int1) * int(int2)

    assert not n % 2, (
        "the lengths of int1 and int2 (n) must be powers of 2 or be of length==1"
    )
    split_idx = n // 2
    a, b = int1[:split_idx], int1[split_idx:]
    c, d = int2[:split_idx], int2[split_idx:]

    ac = _grade_school_int_mult(a, c)
    ad = _grade_school_int_mult(a, d)
    bc = _grade_school_int_mult(b, c)
    bd = _grade_school_int_mult(b, d)
    # recursion

    return int((10**n) * ac + (10**split_idx) * (ad + bc) + bd)  # combine


def grade_school_int_mult(int1: int, int2: int) -> int:
    _val_int_mult_inputs(int1, int2)
    return _grade_school_int_mult(*_prep_int_mult_inputs(str(int1), str(int2)))


def _karatsuba_int_mult(int1: str, int2: str) -> int:
    assert len(int1) == len(int2), "int1 and int2 must have the same length - n"
    n = len(int1)  # convenience

    if n == 1:  # base case
        return int(int1) * int(int2)

    assert not n % 2, (
        "the lengths of int1 and int2 (n) must be powers of 2 or be of length==1"
    )
    split_idx = n // 2
    a, b = int1[:split_idx], int1[split_idx:]
    c, d = int2[:split_idx], int2[split_idx:]
    p, q = _prep_int_mult_inputs(str(int(a) + int(b)), str(int(c) + int(d)))

    ac = _karatsuba_int_mult(a, c)
    bd = _karatsuba_int_mult(b, d)
    pq = _karatsuba_int_mult(p, q)
    # recursion

    adbc = pq - ac - bd
    return int((10**n) * ac + (10**split_idx) * adbc + bd)  # combine


def karatsuba_int_mult(int1: int, int2: int) -> int:
    _val_int_mult_inputs(int1, int2)
    return _karatsuba_int_mult(*_prep_int_mult_inputs(str(int1), str(int2)))
