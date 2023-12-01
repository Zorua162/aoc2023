from day1.day_1_solution import main
import pytest


@pytest.mark.skip("Answer is from AOC website")
def test_data_output():
    output = main("data.txt")
    assert output == "currently unknown"


def test_example_data_output():
    output = main("example_data.txt")
    assert output == ["1", "2", "3", ""]
