from day1.day_1_solution import part1, part2, replace_words
import pytest


def test_example_data_output_part1():
    output = part1("example_data.txt")
    assert output == 142


def test_data_output_part1():
    output = part1("data.txt")
    assert output == 54390


def test_replace_words():
    word_list = ["1one2two", "three3four4"]
    out = replace_words(word_list)
    print(out)
    assert ["1122", "3344"] == out


def test_example_data_output_part2():
    output = part2("example_data_part2.txt")
    assert output == 281


@pytest.mark.skip("Solution is from AOC website")
def test_data_output_part2():
    output = part2("data.txt")
    assert output == "Currently Unknown"
