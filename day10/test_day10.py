from day10.day10_solution import part1, part2
import pytest

current_day = "day10"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 8 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 6882.0 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part2_example_data.txt")
    assert 4 == output


def test_part2_2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part2_example_data_2.txt")
    assert 10 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert "currently unknown" == output
