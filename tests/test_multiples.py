import pytest

from src.multiples import sum_multiples


@pytest.mark.parametrize("quotient, upper_limit, expected",
                         [(3, 10, 18),
                          (5, 0, 0),
                          (5, 5, 0),
                          (5, 6, 5),
                          (5, 10, 5),
                          (5, 11, 15)],
                         )
def test_sum_multiples(quotient, upper_limit, expected):

    result = sum_multiples(quotient, upper_limit)

    assert result == expected

def test__sum_multiples__multiple_calls():

    limit = 16
    sum1 = sum_multiples(3, limit)
    sum2 = sum_multiples(5, limit)
    sum3 = sum_multiples(15, limit)

    total = sum1 + sum2 - sum3

    assert 60 == total
