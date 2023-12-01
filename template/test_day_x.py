from template.day_x_solution import part1, part2
import pytest
current_day = "template"


def test_part1_example_data_output():
    output = part1(f"{current_day}/part1_example_data.txt")
    assert output == ["1", "2", "3", ""]


@pytest.mark.skip("Answer is from AOC website")
def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert output == "currently unknown"


def test_part2_example_data_output():
    output = part2(f"{current_day}/part1_example_data.txt")
    assert output == ["1", "2", "3", ""]


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert output == "currently unknown"
