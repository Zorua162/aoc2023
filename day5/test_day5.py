from day5.day5_solution import (
    part1,
    part2,
    parse_data,
    find_seed_location,
    find_value_in_source_dest_list,
    check_if_valid_location,
    check_if_seed_exists,
)
import pytest

current_day = "day5"


@pytest.fixture
def example_data() -> list:
    data_path = f"{current_day}/part1_example_data.txt"
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n\n") if line != ""]
    return data


@pytest.fixture
def parsed_data(example_data) -> dict:
    return parse_data(example_data)


def test_parse_data(parsed_data) -> None:
    assert [79, 14, 55, 13] == parsed_data["seeds"]
    assert [39, 0, 15] == parsed_data["soil-to-fertilizer"][2]


def test_get_location(parsed_data) -> None:
    location = find_seed_location(79, parsed_data)
    assert 82 == location


def test_find_value_in_source_dest_list() -> None:
    source_dest_list = [[45, 77, 23], [81, 45, 19], [68, 64, 13]]
    assert 45 == find_value_in_source_dest_list(source_dest_list, 77)


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 35 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 282277027 == output


def test_check_if_seed_exists():
    # Lower boundary
    assert not check_if_seed_exists(78, [79, 14, 55, 13])
    assert check_if_seed_exists(79, [79, 14, 55, 13])
    # Upper boundary
    assert check_if_seed_exists(92, [79, 14, 55, 13])
    assert not check_if_seed_exists(93, [79, 14, 55, 13])


def test_check_if_valid_location(parsed_data) -> None:
    assert check_if_valid_location(parsed_data, 82)
    # assert check_if_valid_location(parsed_data, 46)


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 46 == output


@pytest.mark.skip("Answer takes a few mins, so skipping test")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 11554135 == output
