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
    for key, _ in paths.items():
        full_instruction_path_data[key] = follow_full_instructions(
            key, instructions, paths
        )

    return full_instruction_path_data


def in_all_indexes(index: int, last_run_all_z_indexes: list[list[int]]) -> bool:
    for indexes in last_run_all_z_indexes:
        if index not in indexes:
            return False
    return True


def last_run_all_z_at_same_time(
    last_run_all_z_indexes: list[list[int]], instructions_length: int
) -> tuple[bool, int]:
    # Only search through first list, if its not in that list then its not in all
    for index in last_run_all_z_indexes[0]:
        if in_all_indexes(index, last_run_all_z_indexes):
            return True, index + 1
    return False, instructions_length


def find_how_many_steps_all_end_Z(
    instructions: str, starting_locations: list[str], full_instruction_path_data: dict
) -> int:
    locations: list[str] = starting_locations
    last_run_all_z_indexes: list[list[int]] = [[] for _ in locations]
    total_steps = 0
    all_z = False
    while not all_z:
        # Run another iteration of the instructions
        last_run_all_z_indexes = []
        new_locations: list[str] = []
        for location in locations:
            location_data = full_instruction_path_data[location]
            last_run_all_z_indexes.append(location_data["z_indexes"])
            new_locations.append(location_data["end_location"])
        all_z, steps = last_run_all_z_at_same_time(
            last_run_all_z_indexes, len(instructions)
        )
        print(f"steps {steps}")
        locations = new_locations
        total_steps += steps
        print(f"locations {locations} total_steps {total_steps:,}")
    return total_steps


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print(data)
    instructions, paths = parse_data(data)
    starting_locations = get_all_starting_locations(paths)
    full_instruction_path_data = compute_instruction_paths(instructions, paths)
    print(full_instruction_path_data)
    total_steps = find_how_many_steps_all_end_Z(
        instructions, starting_locations, full_instruction_path_data
    )

    return total_steps


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# Submitted answers part 2
# 210700000 too low
# 393,400,000 too low
# 22,715,535,324 too low
