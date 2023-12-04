from day3.day3_solution import (
    part1,
    part2,
    get_all_characters_around_location,
    parse_data,
    remove_uneeded,
    get_other_data,
    merge_data,
    sum_numbers,
)
import pytest

current_day = "day3"


def test_parse_partial_data() -> None:
    data_path = f"{current_day}/part1_partial_data.txt"
    with open(data_path, "r") as f_obj:
        data = f_obj.read().split("\n")[:-1]
    parsed_data: list = parse_data(data)
    print(parsed_data)
    assert {0: ".", 1: ".", 3: ".", 4: "."} == parsed_data[-1]


def test_get_all_characters_around_location_center():
    output = get_all_characters_around_location(1, 1, ["...", ".1.", "..."])
    print(output)
    assert {
        0: ".",
        1: ".",
        2: ".",
        3: ".",
        4: "1",
        5: ".",
        6: ".",
        7: ".",
        8: ".",
    } == output
    assert 9 == len(output)


def test_get_all_characters_around_location_top_left():
    output = get_all_characters_around_location(0, 0, ["...", ".1.", "..."])
    print(output)
    assert {4: ".", 5: ".", 7: ".", 8: "1"} == output
    assert 4 == len(output)


def test_get_all_characters_around_location_bottom_right():
    output = get_all_characters_around_location(2, 2, ["...", ".1.", "..."])
    print(output)
    assert {0: "1", 1: ".", 3: ".", 4: "."} == output
    assert 4 == len(output)


def test_remove_uneeded():
    parsed = parse_data([".....", ".123.", "....."])
    uneeded_removed = remove_uneeded(parsed)
    assert [
        {1: ".", 2: ".", 4: ".", 5: "1", 7: ".", 8: "."},
        {0: ".", 1: ".", 2: ".", 3: ".", 4: "1", 5: "2", 6: ".", 7: ".", 8: "."},
        {0: ".", 1: ".", 2: ".", 3: "1", 4: "2", 5: "3", 6: ".", 7: ".", 8: "."},
        {0: ".", 1: ".", 2: ".", 3: "2", 4: "3", 5: ".", 6: ".", 7: ".", 8: "."},
        {0: ".", 1: ".", 3: "3", 4: ".", 6: ".", 7: "."},
    ] == uneeded_removed


def test_get_other_data():
    adjacent_characters = {
        0: ".",
        1: ".",
        2: ".",
        3: ".",
        4: "1",
        5: "2",
        6: ".",
        7: ".",
        8: "$",
    }
    other_data = get_other_data(adjacent_characters)
    assert "$" == other_data


def test_merge_data():
    parsed = parse_data([".....", ".123.", "....."])
    uneeded_removed = remove_uneeded(parsed)
    merged_data = merge_data(uneeded_removed)
    print(merged_data)
    assert [["123", ""]] == merged_data


def test_merge_multiple():
    parsed = parse_data(["456..", ".123.", ".78.."])
    uneeded_removed = remove_uneeded(parsed)
    merged_data = merge_data(uneeded_removed)
    print(merged_data)
    assert [["456", ""], ["123", ""], ["78", ""]] == merged_data


def test_merge_data_symbol_left():
    parsed = parse_data([".....", "$123.", "....."])
    uneeded_removed = remove_uneeded(parsed)
    merged_data = merge_data(uneeded_removed)
    print(merged_data)
    assert [["123", "$"]] == merged_data


def test_merge_data_symbol_right():
    parsed = parse_data([".....", ".123$", "....."])
    uneeded_removed = remove_uneeded(parsed)
    merged_data = merge_data(uneeded_removed)
    print(merged_data)
    assert [["123", "$"]] == merged_data


def test_merge_data_symbol_above():
    parsed = parse_data(["..$..", ".123.", "....."])
    uneeded_removed = remove_uneeded(parsed)
    merged_data = merge_data(uneeded_removed)
    print(merged_data)
    # Note: may be a bug in the future, if we only want it to see one symbol
    assert [["123", "$$$"]] == merged_data


def test_merge_data_symbol_below():
    parsed = parse_data([".....", ".123.", "..$.."])
    uneeded_removed = remove_uneeded(parsed)
    merged_data = merge_data(uneeded_removed)
    print(merged_data)
    # Note: may be a bug in the future, if we only want it to see one symbol
    assert [["123", "$$$"]] == merged_data


def test_merge_data_symbol_top_right():
    parsed = parse_data(["....$", ".123.", "....."])
    uneeded_removed = remove_uneeded(parsed)
    merged_data = merge_data(uneeded_removed)
    print(merged_data)
    # Note: may be a bug in the future, if we only want it to see one symbol
    assert [["123", "$"]] == merged_data


def test_merge_data_symbol_bottom_left():
    parsed = parse_data([".....", ".123.", "$...."])
    uneeded_removed = remove_uneeded(parsed)
    merged_data = merge_data(uneeded_removed)
    print(merged_data)
    # Note: may be a bug in the future, if we only want it to see one symbol
    assert [["123", "$"]] == merged_data


def test_sum_numbers():
    data = [["1", ""], ["2", "&"], ["3", "$"]]
    output = sum_numbers(data)
    assert 5 == output


def test_part1_example_data_output():
    output = part1(f"{current_day}/part1_example_data.txt")
    assert output == 4361


@pytest.mark.skip("Answer is from AOC website")
def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert output == "currently unknown"


@pytest.mark.skip("Part 2 not started yet")
def test_part2_example_data_output():
    output = part2(f"{current_day}/part1_example_data.txt")
    assert output == ["1", "2", "3", ""]


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert output == "currently unknown"
