from day5.day5_solution import (
    part1,
    part2,
    parse_data,
    expand_seed_sets,
    find_seed_location,
)
import pytest

current_day = "day5"


@pytest.fixture
def example_data() -> list:
    data_path = f"{current_day}/part1_example_data.txt"
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n\n") if line != ""]
    return data


def test_parse_data(example_data) -> None:
    parsed_data = parse_data(example_data)
    print(parsed_data)
    assert [79, 14, 55, 13] == parsed_data["seeds"]
    assert [39, 0, 15] == parsed_data["soil-to-fertilizer"][2]


def test_expand_seed_sets(example_data) -> None:
    parsed_data = parse_data(example_data)
    expanded_seed_data = expand_seed_sets(parsed_data)
    assert 50 == expanded_seed_data["seed-to-soil"][98]


def test_get_location(example_data) -> None:
    parsed_data = parse_data(example_data)
    expanded_seed_data = expand_seed_sets(parsed_data)
    location = find_seed_location(79, expanded_seed_data)
    assert 82 == location


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 35 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert "currently unknown" == output


@pytest.mark.skip("Part 2 not started yet")
def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 0 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert output == "currently unknown"
