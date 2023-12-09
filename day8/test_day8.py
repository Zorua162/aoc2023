from day8.day8_solution import part1, part2, parse_data
import pytest

current_day = "day8"


@pytest.fixture
def example_data() -> list[str]:
    with open(f"{current_day}/part1_example_data.txt", "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print(data)
    return data


def test_parse_data(example_data) -> None:
    parsed_data = parse_data(example_data)
    print(parsed_data)
    assert parsed_data[0] == "RL"
    assert parsed_data[1]["AAA"]["R"] == "CCC"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 2 == output


def test_part1_example_data_output_2() -> None:
    output: int = part1(f"{current_day}/part1_example_data_2.txt")
    assert 6 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 19951 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part2_example_data.txt")
    assert 6 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert "currently unknown" == output
