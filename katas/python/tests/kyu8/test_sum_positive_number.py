from katas.python.kyu8.sum_positive_numbers import positive_sum
import pytest


@pytest.fixture
def test_cases():
    return [
        (15, [1, 2, 3, 4, 5]),
        (13, [1, -2, 3, 4, 5]),
        (9, [-1, 2, 3, 4, -5]),
        (0, []),
        (0, [-1, -2, -3, -4, -5])

    ]


def test_number_in_expanded_form(test_cases):
    for expected_output, input in test_cases:
        assert expected_output == positive_sum(input)
