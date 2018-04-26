import pytest
from katas.python.kyu6.number_in_expanded_form import *


@pytest.fixture
def test_inputs():
    return {
        12: '10 + 2',
        42: '40 + 2',
        123: '100 + 20 + 3',
        70304: '70000 + 300 + 4'
    }


def test_number_in_expanded_form(test_inputs):
    for input, expected_output in test_inputs.items():
        assert expected_output == expanded_form(int(input))