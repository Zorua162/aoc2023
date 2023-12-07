from day7.day7_solution_part1 import (
    part1,
    count_string_occurrences,
    sort_into_kinds,
    rank_bets,
    calc_values,
    sort_values,
)
from day7.day7_solution_part2 import part2
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
        ["AAAAA", "222"],
        ["AAAAK", "333"],
        ["AAAAA", "111"],
        ["AAAA2", "555"],
        ["AAAA3", "666"],
        ["AAAA1", "444"],
    ]
    sorted_values = sort_values(data)
    assert sorted_values[0][0] == "AAAAA"


def test_sort_hands_simple() -> None:
    data = [
        ["A2", "333"],
        ["A1", "222"],
        ["AA", "111"],
    ]

    sorted_values = sort_values(data)
    print(sorted_values)
    assert sorted_values[0][0] == "AA"


def test_rank_bets_single_key() -> None:
    data = [["AAAAK", "222"], ["AAAAQ", "333"], ["AAAAA", "111"]]
    counted = count_string_occurrences(data)
    sorted = sort_into_kinds(counted)
    ranked = rank_bets(sorted)
    print(ranked)
    assert [111, 222, 333] == ranked


def test_rank_bets() -> None:
    data = [
        ["AAAAA", "111"],
        ["99999", "222"],
        ["88888", "333"],
    ]
    counted = count_string_occurrences(data)
    sorted = sort_into_kinds(counted)
    ranked = rank_bets(sorted)
    print(ranked)
    assert [111, 222, 333] == ranked


def test_rank_calc_values() -> None:
    data = [["99999", "222"], ["88888", "333"], ["AAAAA", "111"]]
    counted = count_string_occurrences(data)
    sorted = sort_into_kinds(counted)
    ranked = rank_bets(sorted)
    values = calc_values(ranked)
    print(values)
    assert [333, 444, 333] == values


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 6440 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 253638586 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 5905 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert "currently unknown" == output
