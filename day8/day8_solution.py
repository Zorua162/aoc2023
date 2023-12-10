current_day = "day8"

directions = ["L", "R"]


def parse_data(data: list[str]) -> tuple[str, dict[str, dict[str, str]]]:
    instructions: str = data[0]
    paths: dict[str, dict[str, str]] = {}
    for line in data[1:]:
        split_line = line.split(" = ")
        paths[split_line[0]] = {
            direction: location
            for direction, location in zip(directions, split_line[1][1:-1].split(", "))
        }
    return (instructions, paths)


def step_location(
    location: str, instruction: str, paths: dict[str, dict[str, str]]
) -> str:
    return ""


def search_path(
    location: str, instructions: str, paths: dict[str, dict[str, str]]
) -> list[str]:
    taken_path: list[str] = []
    current_instruction = 0
    print(paths)
    while location != "ZZZ" and len(taken_path) < 100000:
        print(f"location {location} current_instruction { current_instruction}")
        next_direction = instructions[current_instruction]
        print(f"next_direction {next_direction}")
        new_location = paths[location][next_direction]
        taken_path.append(new_location)
        location = new_location
        print(f"new_location {new_location}")
        if current_instruction + 1 > len(instructions) - 1:
            current_instruction = 0
            continue
        current_instruction += 1
    return taken_path


def part1(data_path: str) -> int:
    starting_location = "AAA"
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print(data)
    instructions, paths = parse_data(data)
    taken_path = search_path(starting_location, instructions, paths)
    # print(taken_path)
    return len(taken_path)


def get_all_starting_locations(paths: dict[str, dict[str, str]]) -> list:
    starting_paths = []
    for key in paths.keys():
        if key[2] == "A":
            starting_paths.append(key)
    return starting_paths


def all_locations_end_with_Z(locations: list[str]) -> bool:
    for location in locations:
        if location[2] != "Z":
            return False
    return True


def simultaneously_search_paths(
    locations: list[str], instructions: str, paths: dict[str, dict[str, str]]
) -> list[list[str]]:
    taken_paths: list[list[str]] = [[] for _ in locations]
    current_instruction = 0
    print(paths)
    while not all_locations_end_with_Z(locations):  # and len(taken_paths[0]) < 100000:
        # print(f"new current_instruction {current_instruction} ------------------")
        if len(taken_paths[0]) % 100000 == 0:
            print(f"len(taken_paths[0]) {len(taken_paths[0])} locations {locations}")
        for location_data, taken_path in zip(enumerate(locations), taken_paths):
            location = location_data[1]
            # print(f"location {location} current_instruction {current_instruction}")
            next_direction = instructions[current_instruction]
            # print(f"next_direction {next_direction}")
            new_location = paths[location][next_direction]
            taken_path.append(new_location)
            locations[location_data[0]] = new_location
            # print(f"new_location {new_location}")
        if current_instruction + 1 > len(instructions) - 1:
            current_instruction = 0
            continue
        current_instruction += 1
    return taken_paths


def follow_full_instructions(
    starting_location: str, instructions: str, paths: dict[str, dict[str, str]]
) -> dict:
    path_data: dict = {}
    z_indexes = []
    current_location = starting_location
    for i, instruction in enumerate(instructions):
        current_location = paths[current_location][instruction]
        if current_location[2] == "Z":
            z_indexes.append(i)
    path_data["end_location"] = current_location
    path_data["z_indexes"] = z_indexes

    return path_data


def compute_instruction_paths(
    instructions: str, paths: dict[str, dict[str, str]]
) -> dict:
    full_instruction_path_data: dict[str, dict] = {}
    for key, value in paths.items():
        full_instruction_path_data[key] = follow_full_instructions(
            key, instructions, paths
        )

    return full_instruction_path_data


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print(data)
    instructions, paths = parse_data(data)
    # starting_locations = get_all_starting_locations(paths)
    full_instruction_path_data = compute_instruction_paths(instructions, paths)
    return full_instruction_path_data


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# Submitted answers part 2
# 210700000 too low
# 393400000 too low
