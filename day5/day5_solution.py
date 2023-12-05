current_day = "day5"


def parse_data(data: list) -> dict:
    """Parsed the input data into a form thats easier to work with

    Args:
        data (list): the input data

    Returns:
        list:
    """
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
            [value for value in values.split(" ")]
            for values in key_data.split("\n")
            if values != ""
        ]

    return parsed_data


def expand_seed_sets(parsed_data: dict) -> dict:
    keys = [key for key in parsed_data.keys() if key != "seeds"]
    for key in keys:
        data = parsed_data[key]
        current_key_dict: dict = {}
        for source_dest_set in data:
            current_key_dict.update(
                zip(
                    range(
                        int(source_dest_set[0]),
                        int(source_dest_set[0]) + int(source_dest_set[2]),
                    ),
                    range(
                        int(source_dest_set[1]),
                        int(source_dest_set[1]) + int(source_dest_set[2]),
                    ),
                )
            )

        parsed_data[key] = current_key_dict

    return parsed_data


def find_seed_location(seed: int, parsed_data: dict) -> int:
    current_value = seed
    keys = [key for key in parsed_data.keys() if key != "seeds"]
    for key in keys:
        current_dict = parsed_data[key]
        print(
            f"Current key is {key}, current value is {current_value}, "
            f"current dict is {current_dict}"
        )
        current_value = current_dict[current_value]
    return current_value


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n\n") if line != ""]
    parsed_data = parse_data(data)
    parsed_data = expand_seed_sets(parsed_data)
    location = find_seed_location(79, parsed_data)
    print(location)
    return 0


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
        print(data)
    return 0


if __name__ == "__main__":
    print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
