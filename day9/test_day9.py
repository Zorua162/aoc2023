from day9.day9_solution import (
    part1,
    part2,
    find_polynomial_degree,
    find_value,
    determine_coefficients,
    calculate_coefficients,
    all_0,
)
import pytest

current_day = "day9"
correct_example_files = [
    f"{current_day}/part1_example_data.txt",
    f"{current_day}/data.txt",
]
real_data = [
    7,
    8,
    7,
    15,
    65,
    227,
    628,
    1477,
    3095,
    5950,
    10697,
    18223,
    29697,
    46625,
    70910,
    104917,
    151543,
    214292,
    297355,
    405695,
    545137,
]


def test_all_0() -> None:
    not_all_0 = [1, 0, -3]
    assert not all_0(not_all_0)
    all_0_items = [0, 0, 0]
    assert all_0(all_0_items)


def test_find_polynomial_degree() -> None:
    degree_1 = [0, 3, 6, 9, 12, 15]
    assert 1 == find_polynomial_degree(degree_1)
    assert 6 == find_polynomial_degree(real_data)


def test_calculate_coefficients_degree_1() -> None:
    data = [0, 3, 6, 9, 12, 15]
    degree = 1
    coefficients = calculate_coefficients(data, degree)
    print(coefficients)
    assert [0, 3] == coefficients


def test_calculate_coefficients_degree_2() -> None:
    data = [1, 3, 6, 10, 15, 21]
    degree = find_polynomial_degree(data)
    coefficients = calculate_coefficients(data, degree)
    print(coefficients)
    assert [1, 1.5, 0.5] == coefficients


def test_determine_coefficients() -> None:
    data = [[0, 3, 6, 9, 12, 15]]
    degrees = [1]
    coefficients = determine_coefficients(data, degrees)
    assert [[0, 3]] == coefficients


def test_find_value() -> None:
    data = [0, 3, 6, 9, 12, 15]
    coefficient = [0, 3]
    assert 18 == find_value(coefficient, len(data))


def test_real_line_2() -> None:
    real_coefficients = determine_coefficients([real_data], [6])
    assert real_data[1] == round(find_value(real_coefficients[0], 1))


@pytest.mark.skip("Currently failing")
@pytest.mark.parametrize("data_path", correct_example_files)
def test_existing_values_correct_example(data_path) -> None:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    parsed_data = [[int(number) for number in line.split(" ")] for line in data]
    degrees = [find_polynomial_degree(line) for line in parsed_data]
    coefficients = determine_coefficients(parsed_data, degrees)
    incorrect_values = []
    for line, coefficient in zip(data, coefficients):
        for i, value in enumerate(line.split(" ")):
            calculated_value = find_value(coefficient, i)
            print(
                f"actual value is {value}, calculated_value is "
                f"{calculated_value} in line {repr(line)}"
            )

            # assert int(value) == round(calculated_value)
            if int(value) != round(calculated_value):
                incorrect_values.append(
                    [int(value), round(calculated_value), calculated_value]
                )
    print(incorrect_values)
    print(len(incorrect_values))
    assert [] == incorrect_values


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 114 == round(output)


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
