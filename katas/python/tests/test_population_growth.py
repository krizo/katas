from katas.python.population_growth import nb_year
import pytest

@pytest.fixture
def population_growth_test_inputs():
    return [
        (1000, 2, 50, 1200, 3),
        (1500, 5, 100, 5000, 15),
        (1500000, 2.5, 10000, 2000000, 10),
        (1500000, 0.25, 1000, 2000000, 94)
    ]


def test_population_growth(population_growth_test_inputs):
    for initial_inhabitants, natural_growth_perc, immigrants, target_population, expected_years_of_growth \
            in population_growth_test_inputs:
        assert nb_year(initial_inhabitants, natural_growth_perc, immigrants, target_population) \
               == expected_years_of_growth
