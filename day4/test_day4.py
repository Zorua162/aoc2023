from day4.day4_solution import part1, part2
import pytest

current_day = "day4"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 13 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 22674 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part2_example_data.txt")
    assert 30 == output


@pytest.mark.skip(
    "Passes, however is a very slow solution, so skipping to save " "resources"
)
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 5747443 == output
