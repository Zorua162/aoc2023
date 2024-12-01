from typing import Optional

current_day = "day3"
POSSIBLE_SINGLE_NUMBERS = [str(i) for i in range(10)]
NON_SYMBOL_CHARACTERS = POSSIBLE_SINGLE_NUMBERS.copy()
NON_SYMBOL_CHARACTERS.append(".")


def get_char(
    i: int, j: int, data: list[str], already_scanned: list[list[int]]
) -> tuple[Optional[str], list[list[int]]]:
    if within_grid(i, j, data) and [i, j] not in already_scanned:
        char = data[i][j]
        if char in POSSIBLE_SINGLE_NUMBERS:
            already_scanned.append([i, j])
            return char, already_scanned
    return None, already_scanned


def search_direction(
    i: int,
    j: int,
    char: str,
    direction: int,
    data: list,
    already_scanned: list[list[int]],
) -> tuple[str, list[list[int]]]:
    search_value = direction
    new_char: Optional[str] = ""

    while new_char is not None:
        if direction < 0:
            char = new_char + char
        else:
            char = char + new_char
        char_out = get_char(i, j + search_value, data, already_scanned)
        new_char = char_out[0]
        already_scanned = char_out[1]
        search_value += direction

    return char, already_scanned


def find_rest_of_number(
    i: int, j: int, char: str, data: list, already_scanned: list[list[int]]
) -> tuple[int, list[list[int]]]:
    # Search one left and one right of number
    directions = [1, -1]
    for direction in directions:
        char_out = search_direction(i, j, char, direction, data, already_scanned)
        char = char_out[0]
        already_scanned = char_out[1]

    return int(char), already_scanned


def within_grid(i: int, j: int, data: list[str]):
    return i <= len(data) - 1 and j + 1 <= len(data[i]) and i >= 0 and j >= 0


def search_for_numbers(i: int, j: int, data: list[str]) -> list:
    found_numbers = []
    already_scanned: list[list[int]] = []
    for k in range(-1, 2):
        for n in range(-1, 2):
            # print(f"len data[0] {len(data)} i+k {i+k}")
            if (
                within_grid(i + k, j + n, data)
                and not n == k == 0
                and [i + k, j + n] not in already_scanned
            ):
                char = data[i + k][j + n]
                if char in POSSIBLE_SINGLE_NUMBERS:
                    number_out = find_rest_of_number(
                        i + k, j + n, char, data, already_scanned
                    )
                    number = number_out[0]
                    already_scanned = number_out[1]
                    found_numbers.append(number)
    # [[[i, j], char], [[i, j], char]]
    return found_numbers


def find_valid_part_numbers(data: list) -> list:
    valid_part_numbers: list[int] = []
    for i, line in enumerate(data):
        for j, character in enumerate(line):
            if character not in NON_SYMBOL_CHARACTERS:
                # Search around the symbol for any numbers
                numbers = search_for_numbers(i, j, data)
                valid_part_numbers.extend(numbers)
    return valid_part_numbers


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    # parsed_data: list = parse_data(data)
    valid_part_numbers = find_valid_part_numbers(data)
    print(f"There are {len(valid_part_numbers)} valid part numbers")
    total = 0
    for number in valid_part_numbers:
        total += number

    return total


def find_gears(data: list) -> list:
    gear_ratios: list[int] = []
    for i, line in enumerate(data):
        for j, character in enumerate(line):
            if character == "*":
                # Search around the symbol for any numbers
                numbers = search_for_numbers(i, j, data)
                if len(numbers) == 2:
                    ratio = numbers[0] * numbers[1]
                    gear_ratios.append(ratio)
                # valid_part_numbers.extend(numbers)
    return gear_ratios


def part2(data_path):
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    # parsed_data: list = parse_data(data)
    gear_ratios = find_gears(data)
    print(f"There are {len(gear_ratios)} valid gear ratios")
    total = 0
    for number in gear_ratios:
        total += number

    return total


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/part1_partial_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# Incorrect submitted answers
# 1,420,741 too high
# 1,419,826 too high
# 1,634,187 too high
# Correct:
# 521,515, correct!

# Part 2:
# 69527306, correct!
