from day7.day7_solution import (
    part1,
    part2,
    count_string_occurrences,
    sort_into_kinds,
    rank_bets,
    calc_values,
    get_adjusted_value_of_string,
)
import pytest

current_day = "day7"


def test_five() -> None:
    data = [["AAAAA", "1"]]
    counted = count_string_occurrences(data)
    sorted = sort_into_kinds(counted)
    print(sorted)
    assert 1 == len(sorted["five"])


def test_four() -> None:
    data = [["AAAAB", "1"]]
    counted = count_string_occurrences(data)
    sorted = sort_into_kinds(counted)
    print(sorted)
    assert 1 == len(sorted["four"])


def test_full() -> None:
    data = [["AAABB", "1"]]
    counted = count_string_occurrences(data)
    sorted = sort_into_kinds(counted)
    print(sorted)
    assert 1 == len(sorted["full"])


def test_three() -> None:
    data = [["AAABC", "1"]]
    counted = count_string_occurrences(data)
    sorted = sort_into_kinds(counted)
    print(sorted)
    assert 1 == len(sorted["three"])


def test_two_pair() -> None:
    data = [["AABBC", "1"]]
    counted = count_string_occurrences(data)
    sorted = sort_into_kinds(counted)
    print(sorted)
    assert 1 == len(sorted["two_pair"])


def test_one_pair() -> None:
    data = [["AABCD", "1"]]
    counted = count_string_occurrences(data)
    sorted = sort_into_kinds(counted)
    print(sorted)
    assert 1 == len(sorted["one_pair"])


def test_high() -> None:
    data = [["ABCDE", "1"]]
    counted = count_string_occurrences(data)
    sorted = sort_into_kinds(counted)
    print(sorted)
    assert 1 == len(sorted["high"])


def test_sort_hands() -> None:
    data = [
        ["AAAAC", "222"],
        ["AAAAD", "333"],
        ["AAAAB", "111"],
        ["AAAA2", "555"],
        ["AAAA3", "666"],
        ["AAAA1", "444"],
    ]
    adjusted = get_adjusted_value_of_string(data)
    sorted_values = sorted(adjusted, key=lambda x: x[2])
    assert sorted_values[0][0] == "AAAAB"


def test_sort_hands_simple() -> None:
    data = [
        ["A2", "333"],
        ["A1", "222"],
        ["AA", "111"],
    ]
    adjusted = get_adjusted_value_of_string(data)
    print(adjusted)
    sorted_values = sorted(adjusted, key=lambda x: x[2])
    assert sorted_values[0][0] == "AA"


def test_rank_bets_single_key() -> None:
    data = [["AAAAC", "222"], ["AAAAD", "333"], ["AAAAB", "111"]]
    counted = count_string_occurrences(data)
    adjusted = get_adjusted_value_of_string(counted)
    sorted = sort_into_kinds(adjusted)
    ranked = rank_bets(sorted)
    print(ranked)
    assert [111, 222, 333] == ranked


def test_rank_bets() -> None:
    data = [
        ["CCCCC", "666"],
        ["AAAAA", "444"],
        ["BBBBB", "555"],
        ["AAAAC", "222"],
        ["AAAAD", "333"],
        ["AAAAB", "111"],
    ]
    counted = count_string_occurrences(data)
    adjusted = get_adjusted_value_of_string(counted)
    sorted = sort_into_kinds(adjusted)
    ranked = rank_bets(sorted)
    print(ranked)
    assert [444, 555, 666, 111, 222, 333] == ranked


def test_rank_bets_numbers() -> None:
    data = [
        ["AAAAC", "222"],
        ["AAAAD", "333"],
        ["AAAAB", "111"],
        ["AAAA2", "555"],
        ["AAAA3", "666"],
        ["AAAA1", "444"],
    ]
    counted = count_string_occurrences(data)
    adjusted = get_adjusted_value_of_string(counted)
    sorted = sort_into_kinds(adjusted)
    ranked = rank_bets(sorted)
    print(ranked)
    assert [111, 222, 333, 444, 555, 666] == ranked


def test_rank_calc_values() -> None:
    data = [["AAAAC", "222"], ["AAAAD", "333"], ["AAAAB", "111"]]
    counted = count_string_occurrences(data)
    adjusted = get_adjusted_value_of_string(counted)
    sorted = sort_into_kinds(adjusted)
    ranked = rank_bets(sorted)
    values = calc_values(ranked)
    print(values)
    assert [333, 444, 333] == values


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 6440 == output


@pytest.mark.skip("Currently failing")
def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 0 == output


@pytest.mark.skip("Part 2 not started yet")
def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 0 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert "currently unknown" == output
