import pytest
from reports.average_gdp import generate_average_gdp_report

def test_single_country():
    data = [
        {"country": "USA", "gdp": "25462"},
        {"country": "USA", "gdp": "23315"}
    ]
    result = generate_average_gdp_report(data)

    assert len(result) == 1
    assert result[0]["country"] == "USA"
    assert result[0]["avg_gdp"] == 24388.5


def test_sorting():
    data = [
        {"country": "USA", "gdp": "25000"},
        {"country": "China", "gdp": "18000"}
    ]
    result = generate_average_gdp_report(data)

    assert result[0]["country"] == "USA"
    assert result[1]["country"] == "China"


def test_multiple_years():
    data = [
        {"country": "USA", "gdp": "25462"},
        {"country": "USA", "gdp": "23315"},
        {"country": "USA", "gdp": "22994"}
    ]
    result = generate_average_gdp_report(data)

    assert abs(result[0]["avg_gdp"] - 23923.67) < 0.01

