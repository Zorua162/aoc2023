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
