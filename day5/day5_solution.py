import numpy as np

current_day = "day5"


def parse_data(data: list) -> dict:
    """Parsed the input data into a form thats easier to work with

    Args:
        data (list): the input data

    Returns:
        list:
    """
    print("Parsing data")
    parsed_data: dict = {}
    for data_set in data:
        split_data_set = data_set.split(":")
        parsed_data[split_data_set[0]] = split_data_set[1]

    # Parsed the seed numbers
    parsed_data["seeds"] = [
        int(number) for number in parsed_data["seeds"].split(" ") if number != ""
    ]

    keys = [key for key in parsed_data.keys() if key != "seeds"]
    for old_key in keys:
        key_data = parsed_data[old_key]
        # Remove the old key name
        del parsed_data[old_key]
        new_key = old_key[:-4]
        # Put the data in with the new key name
        parsed_data[new_key] = [
            [int(value) for value in values.split(" ")]
            for values in key_data.split("\n")
            if values != ""
        ]

    return parsed_data


def find_value_in_source_dest_list(
    source_dest_list: list, value: int, reverse=False
) -> int:
    """Takes in the destination source list and a value to find in it and output its
    corresponding value

    Args:
        source_dest_list (list): list of lists of dest source range values
        value (int): value to find in these lists

    Returns:
        int: the found value, or the original value if it wasn't found
    """

    for dest_source_range_list in source_dest_list:
        destination = dest_source_range_list[0]
        source = dest_source_range_list[1]
        ds_range = dest_source_range_list[2]
        diff = source - destination
        # print(f"src {source} dst {destination}")
        if not reverse:
            if value >= source and value < source + ds_range:
                return value - diff
        else:
            if value >= destination and value < destination + ds_range:
                return value + diff

    return value


def find_seed_location(seed: int, parsed_data: dict, reverse=False) -> int:
    current_value = seed
    keys = [key for key in parsed_data.keys() if key != "seeds"]
    if reverse:
        keys = list(reversed(keys))
    for key in keys:
        current_source_dest_list = parsed_data[key]
        # print(
        #     f"Current key is {key}, current value is {current_value}, "
        #     f"current source dest list is {current_source_dest_list}"
        # )
        current_value = find_value_in_source_dest_list(
            current_source_dest_list, current_value, reverse=reverse
        )
    return current_value


def find_lowest_seed_location(expanded_seed_data: dict):
    lowest_location = np.inf
    for seed in expanded_seed_data["seeds"]:
        print(f"Starting on seed {seed}")
        location = find_seed_location(seed, expanded_seed_data)
        if location < lowest_location:
            print(f"Found new lowest! Seed: {seed} with location {location}")
            lowest_location = location
    return lowest_location


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n\n") if line != ""]
    parsed_data = parse_data(data)
    return find_lowest_seed_location(parsed_data)


def find_number_of_locations(parsed_data: dict):
    possible_locations = 0
    for location in parsed_data["humidity-to-location"]:
        possible_locations += location[2]
    print(f"There are {possible_locations:,} possible locations and one lowest one")


def check_if_seed_exists(seed_number: int, seed_data: list) -> bool:
    for i in range(0, len(seed_data), 2):
        if (
            seed_number >= seed_data[i]
            and seed_number < seed_data[i] + seed_data[i + 1]
        ):
            return True
    return False


def check_if_valid_location(parsed_data: dict, current_location: int) -> bool:
    """Go backwards through the dest source lists to find if a seed corresponds to the
    location
    """
    seed_number = find_seed_location(current_location, parsed_data, True)
    return check_if_seed_exists(seed_number, parsed_data["seeds"])


def part2(data_path: str) -> int:
    """Plan is to start at the lowest possible location and check if its valid,
    increasing the location spot until a valid destination is found and that is the
    lowest location"""
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n\n") if line != ""]
    parsed_data = parse_data(data)
    lowest_location = 0
    while not check_if_valid_location(parsed_data, lowest_location):
        if lowest_location % 10000 == 0:
            print(f"Failed check for {lowest_location:,}")
        lowest_location += 1
    print(f"Lowest location was found to be: {lowest_location}")
    return lowest_location
    # return find_lowest_seed_location(parsed_data)


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))
