from katas.python.kyu6.good_vs_evil import goodVsEvil


def test_good_vs_evil():
    assert goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1') == 'Battle Result: Evil eradicates all trace of Good'
    assert goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0') == 'Battle Result: Good triumphs over Evil'
    assert goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0') == 'Battle Result: No victor on this battle field'