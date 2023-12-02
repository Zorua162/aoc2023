from day2.day2_solution import (
    part1,
    part2,
    parse_data,
    find_fewest_cubes_per_game,
    power_values,
)
import pytest

current_day = "day2"

input_data: list = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "",
]


def test_part1_example_data_output():
    output = part1(f"{current_day}/part1_example_data.txt")
    assert output == 8


def test_parsed_data() -> None:
    parsed_data = parse_data(input_data)
    print(parsed_data)
    assert parsed_data[1][0]["blue"] == 3
    assert parsed_data[2][1]["green"] == 3
    assert parsed_data[2][1]["blue"] == 4
    assert parsed_data[4][2]["red"] == 14


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert output == 2285


def test_find_highest():
    parsed_data = parse_data(input_data)
    output = find_fewest_cubes_per_game(parsed_data)
    assert output[1]["blue"] == 6


# def test_sum_cubes():
#     parsed_data = parse_data(input_data)
#     fewest_cubes = find_fewest_cubes_per_game(parsed_data)
#     output = sum_power_of_cubes(fewest_cubes)
#     assert output["blue"] == 6


def test_power_values():
    values = [1, 2, 3]
    output = power_values(values)
    assert output == 6


def test_part2_example_data_output():
    output = part2(f"{current_day}/part1_example_data.txt")
    assert output == 2286


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert output == "currently unknown"
