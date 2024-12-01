current_day = "day6"


def parse_line(line_data: str) -> list[int]:
    return [
        int(item) for item in line_data.split(" ") if item != "" and ":" not in item
    ]


def parse_data(data: list) -> dict:
    """Parse the times and distances out of the data

    Args:
        data (list): The data input

    Returns:
        dict: A dictionary with keys containing the lists of information
    """
    time_line = data[0]
    distance_line = data[1]
    parsed_data = {"time": parse_line(time_line), "distance": parse_line(distance_line)}
    return parsed_data


def calculate_possible_distances_for_time(time: int) -> list:
    # Hold button down for 0ms to length of race and calculate the distances gone
    distances = []
    for i in range(time + 1):
        if i % 1000 == 0:
            print(f"Checking time {i}")
        distances.append(i * (time - i))
    return distances


def calculate_all_distances(times: list) -> list[list]:
    time_list = []
    for time in times:
        time_list.append(calculate_possible_distances_for_time(time))
    return time_list


def count_winning_strategies(all_distances: list[list[int]], max_distances: list[int]):
    counts = []
    for distances, max_distance in zip(all_distances, max_distances):
        count = 0
        for distance in distances:
            if distance > max_distance:
                count += 1
        counts.append(count)
    return counts


def product_values(values: list) -> int:
    # Reused from day 2
    total_value: int = 0
    for value in values:
        if total_value == 0:
            total_value = value
            continue
        total_value *= value
    return total_value


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    parsed_data = parse_data(data)
    all_distances = calculate_all_distances(parsed_data["time"])
    number_of_possible_winning_strategies = count_winning_strategies(
        all_distances, parsed_data["distance"]
    )
    return product_values(number_of_possible_winning_strategies)


def join_ints(ints_to_join: list[int]) -> int:
    strs_to_join = [str(i) for i in ints_to_join]
    joined_str = "".join(strs_to_join)
    return int(joined_str)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    parsed_data = parse_data(data)
    time = join_ints(parsed_data["time"])
    max_distance = join_ints(parsed_data["distance"])
    distances = calculate_possible_distances_for_time(time)
    possible_winning_strategies = count_winning_strategies([distances], [max_distance])
    return possible_winning_strategies[0]


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))
