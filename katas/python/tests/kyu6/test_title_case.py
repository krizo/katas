import pytest
from katas.python.kyu6.title_case import title_case



def test_title_case():
    assert 'A Clash of Kings' == title_case('a clash of KINGS', 'a an the of')
    assert 'The Wind in the Willows' == title_case('THE WIND IN THE WILLOWS', 'The In')
    assert 'The Quick Brown Fox' == title_case('the quick brown fox')