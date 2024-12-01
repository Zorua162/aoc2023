from day3.day3_solution import (
    part1,
    part2,
    find_valid_part_numbers,
)

current_day = "day3"


def test_find_valid_part_numbers_left():
    data = [".....", "$123.", "....."]
    output = find_valid_part_numbers(data)
    assert [123] == output


def test_find_valid_part_numbers_right():
    data = [".....", ".123$", "....."]
    output = find_valid_part_numbers(data)
    assert [123] == output


def test_find_valid_part_numbers_below():
    data = ["..$..", ".123.", "....."]
    output = find_valid_part_numbers(data)
    assert [123] == output


def test_find_valid_part_numbers_above():
    data = [".....", ".123.", "..$.."]
    output = find_valid_part_numbers(data)
    assert [123] == output


def test_part1_example_data_output():
    output = part1(f"{current_day}/part1_example_data.txt")
    assert 4361 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 521515 == output


def test_part2_example_data_output():
    output = part2(f"{current_day}/part1_example_data.txt")
    assert 467835 == output


def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 69527306 == output
