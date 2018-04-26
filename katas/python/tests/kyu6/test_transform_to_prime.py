import pytest
from katas.python.kyu6.transform_to_prime import minimum_number


@pytest.fixture
def test_inputs():
    return [
        ([3, 1, 2], 1),
        ([5, 2], 0),
        ([1, 1, 1], 0),
        ([2, 12, 8, 4, 6], 5),
        ([50, 39, 49, 6, 17, 28], 2)
    ]


def test_to_prime(test_inputs):
    for input, expected_output in test_inputs:
        assert expected_output == minimum_number(input)
