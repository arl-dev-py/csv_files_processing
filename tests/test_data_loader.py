import pytest
from data_loader import load_csv_files

def test_load_single_file():
    data = load_csv_files(["test_data/sample.csv"])

    assert len(data) == 3
    assert data[0]["country"] == "United States"
    assert float(data[0]["gdp"]) == 25462

def test_load_multiple_files():
    data = load_csv_files(['test_data/file1.csv', 'test_data/file2.csv'])

    assert len(data) == 4
    assert data[0]['country'] == 'Russia'
    assert data[2]['country'] == 'USA'


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv_files(["test_data/nonexistent.csv"])
