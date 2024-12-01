from day6.day6_solution import (
    part1,
    part2,
    parse_line,
    parse_data,
    calculate_possible_distances_for_time,
    calculate_all_distances,
    count_winning_strategies,
    join_ints,
)
import pytest

current_day = "day6"


@pytest.fixture
def example_data() -> list:
    with open(f"{current_day}/part1_example_data.txt", "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    return data


@pytest.fixture
def parsed_data() -> dict:
    with open(f"{current_day}/part1_example_data.txt", "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    return parse_data(data)


def test_parse_line(example_data):
    assert 7 == parse_line(example_data[0])[0]


def test_parse_data(example_data):
    assert [7, 15, 30] == parse_data(example_data)["time"]


def test_calculate_possible_distances():
    output = calculate_possible_distances_for_time(7)
    assert [0, 6, 10, 12, 12, 10, 6, 0] == output


def test_calculate_all_distances():
    output = calculate_all_distances([7, 8])
    print(output)
    assert [0, 6, 10, 12, 12, 10, 6, 0] == output[0]


def test_count_winning_strategies(parsed_data):
    all_distances = calculate_all_distances(parsed_data["time"])
    count_of_winning_strats = count_winning_strategies(
        all_distances, parsed_data["distance"]
    )
    assert [4, 8, 9] == count_of_winning_strats


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 288 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 505494 == output


def test_join_ints():
    output = join_ints([1, 2, 3])
    assert 123 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 71503 == output


# Takes ~ 11s
@pytest.mark.skip("Too slow for running in test suite")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 23632299 == output
