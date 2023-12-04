current_day = "day3"
POSSIBLE_SINGLE_NUMBERS = [str(i) for i in range(10)]


def get_all_characters_around_location(i: int, j: int, data: list) -> dict:
    character_adjacents: dict = {}
    for k in range(-1, 2):
        for n in range(-1, 2):
            print(f"len data[0] {len(data)} i+k {i+k}")
            if (
                i + k <= len(data) - 1
                and j + n + 1 <= len(data[i])
                and i + k >= 0
                and j + n >= 0
            ):
                # print(f"i {i} j {j} k {k} n {n} line {data[i+k]}")
                character_adjacents.update({(k + 1) * 3 + (n + 1): data[i + k][j + n]})
    return character_adjacents


def parse_data(data: list) -> list:
    parsed_data = []
    print(f"data len{len(data)}")
    for i in range(len(data)):
        for j in range(len(data[i])):
            parsed_data.append(get_all_characters_around_location(i, j, data))
    return parsed_data


def middle_row_has_number(adjacent_characters: dict) -> bool:
    check_keys = [3, 4, 5]
    existing_check_keys = [
        key for key in check_keys if key in adjacent_characters.keys()
    ]
    for key in existing_check_keys:
        if adjacent_characters[key] != ".":
            return True
    return False


def remove_uneeded(parsed_data: list) -> list:
    """Remove uneeded rows for doing part1"""
    # Assume no vertical numbers for the moment
    # Therefore get rid of any rows that don't have ny numbers in the middle
    uneeded_removed = [
        adjacent_characters
        for adjacent_characters in parsed_data
        if middle_row_has_number(adjacent_characters)
    ]
    return uneeded_removed


def get_other_data(adjacent_characters: dict) -> str:
    other_data = ""
    for value in adjacent_characters.values():
        if value != "." and value not in POSSIBLE_SINGLE_NUMBERS:
            other_data += value
    return other_data


def merge_data(parsed_data: list) -> list:
    """Loop through each parsed item, and find the numbers next to it"""
    number_data: list = []
    current_number = ""
    other_data = ""
    for adjacent_characters in parsed_data:
        print(adjacent_characters)
        if adjacent_characters[4] in POSSIBLE_SINGLE_NUMBERS:
            current_number += adjacent_characters[4]
            other_data += get_other_data(adjacent_characters)
        else:
            if current_number != "":
                number_data.append([current_number, other_data])
            current_number = ""
            other_data = ""

    return number_data


def sum_numbers(number_data: list) -> int:
    total = 0
    for item in number_data:
        number = item[0]
        other_data = item[1]
        if other_data != "":
            print(
                f"Adding number {number}, with other_data {other_data} current "
                f"total is {total}"
            )
            total += int(number)
        else:
            print(f"Not adding {number}, with other_data {other_data}")
    return total


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = f_obj.read().split("\n")[:-1]
    parsed_data: list = parse_data(data)
    # uneeded_removed = remove_uneeded(parsed_data)
    # merged_data = merge_data(uneeded_removed)
    merged_data = merge_data(parsed_data)
    print(merged_data)
    total_sum: int = sum_numbers(merged_data)
    print(f"Length of merged data {len(merged_data)}")

    return total_sum


def part2(data_path):
    with open(data_path, "r") as f_obj:
        data = f_obj.read().split("\n")
    print(data)
    return data


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/part1_partial_data.txt"))
    print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))

# Incorrect submitted answers
# 1420741 too high
# 1419826 too high
# 1634187 too high
