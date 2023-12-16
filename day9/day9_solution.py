import numpy as np

current_day = "day9"


def all_0(diffs: list[int]) -> bool:
    for item in diffs:
        if item != 0:
            return False
    return True


def find_polynomial_degree(line: list[int]) -> int:
    diffs = line
    print(f"Starting line is {line}")
    degree = 0
    while not all_0(diffs):
        # print(f"diffs {diffs}")
        diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
        degree += 1
        print(f"iteration {degree} diffs {diffs}")
    end_degree = degree - 1
    if end_degree < 0:
        raise Exception("End degree < 0")
    return end_degree


def calculate_coefficients(line: list[int], degree: int) -> list[int]:
    print(f"Starting new coefficients, degree {degree}")
    # Create a list of equations, based on the degree
    truncated_line = line[: degree + 1]
    # x = np.transpose(np.array(truncated_line))
    x = np.array(truncated_line, dtype="float64")
    # x^2 + x^1 + x^0
    # 0a c
    # 1a c
    range_degree = range(degree + 1)
    A = [[i**j for j in range_degree] for i in range_degree]
    np_A = np.array(A, dtype="float64")
    inv_A = np.linalg.inv(np_A)
    print(f"inv_A {inv_A} x {x}")
    coefficients = np.matmul(inv_A, x)
    return [i for i in coefficients.tolist()]


def determine_coefficients(
    parsed_data: list[list[int]], degrees: list[int]
) -> list[list[int]]:
    coefficients: list[list[int]] = []
    for data, degree in zip(parsed_data, degrees):
        coefficients.append(calculate_coefficients(data, degree))
    # Solve simultaneous equations to find the coefficients
    return coefficients


def find_value(coefficients: list[int], value_number: int) -> int:
    values = [
        coefficient * value_number ** (i) for i, coefficient in enumerate(coefficients)
    ]
    equation = [
        f"{coefficient} x {value_number} ^ {i}"
        for i, coefficient in enumerate(coefficients)
    ]
    print(f"\nfind_value equation {' + '.join(equation)} values {values}")
    return sum(values)


def calculate_next_value(line: str) -> int:
    #
    return 0


def simple_part_1(data: list[str]) -> int:
    total = 0
    for line in data:
        next_value = calculate_next_value(line)
        total += next_value
    return total


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    parsed_data = [[int(number) for number in line.split(" ")] for line in data]
    degrees = [find_polynomial_degree(line) for line in parsed_data]
    coefficients = determine_coefficients(parsed_data, degrees)
    next_values = [
        find_value(coefficient, len(data))
        for coefficient, data in zip(coefficients, parsed_data)
    ]
    print(f"next_values {next_values}")
    return sum(next_values)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
        print(data)
    return 0


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))

# Submitted answers
# 1584748570 too high
# 1584748569 too high
