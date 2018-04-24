import pytest
from katas.python.find_divisiors import divisors


@pytest.fixture
def test_inputs():
    return {
        "12": [2, 3, 4, 6],
        "25": [5],
        "13": "13 is prime"
    }


def test_find_divisors(test_inputs):
    for input, expected_output in test_inputs.items():
        assert expected_output == divisors(int(input))