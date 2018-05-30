import pytest
from katas.python.kyu7.find_sum_when_not_negative import find_sum


@pytest.fixture
def test_cases():
    return [
        ([1, 3, 5], 9),
        # (None, 0),
        ([1, -2, 4], -1),
        ([0], 0),
        ([1, 1, 5], 7),
        ([1, 1, 1, 1, 1, 1, 1, 1, 0], 8),
        ([-1, -1, 5], -1),
        ([-1, -1, -5], -1),
        ([0, -1, 5], -1),
        ([0, 0, 0], 0)
    ]


def test_find_sum(test_cases):
    for input_args, expected_result in test_cases:
        if input_args is None:
            assert find_sum(*input_args) == 0
        assert find_sum(*input_args) == expected_result
