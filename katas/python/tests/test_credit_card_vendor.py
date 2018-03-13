from katas.python.credit_card_vendor import *
import pytest


@pytest.fixture
def card_numbers():
    return [
        ("VISA", 4111111111111111),
        ("AMEX", 378282246310005),
        ("VISA", 4111111111111),
        ("Unknown", 41111111111111),
        ("VISA", 4012888888881881),
        ("Discover", 6011111111111117),
        ("Mastercard", 5105105105105100),
        ("Mastercard", 5105105105105106),
        ("Unknown", 9111111111111111),
        ("Unknown", 123),
        ("Unknown", None)
    ]


def test_card_numbers(card_numbers):
    for vendor, number in card_numbers:
        assert get_issuer(number) == vendor
