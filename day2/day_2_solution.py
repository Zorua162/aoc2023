from collections import defaultdict

current_day = "day2"


def parse_game_data(game_data: str) -> list:
    game_list: list = []
    for hand in game_data.split("; "):
        current_hand = {}
        for cube_type in hand.split(", "):
            split_cube_type = cube_type.split(" ")
            current_hand[split_cube_type[1]] = int(split_cube_type[0])
        game_list.append(current_hand)
    return game_list


def parse_game(parsed_data: dict, game: str) -> dict:
    split_game = game.split(": ")
    game_id = split_game[0].split(" ")[1]

    # parsed_data[int(game[5])] = [
    #     {cube_set[2:]: int(cube_set[0]) for cube_set in hand.split(", ")}
    #     for hand in game_hands
    # ]
    parsed_data[int(game_id)] = parse_game_data(split_game[1])
    return parsed_data


def parse_data(data: list) -> dict[int, list]:
    """Returns a list of dicts which contain the data for each handful"""
    parsed_data: dict[int, list] = {}
    for game in data:
        if game == "":
            continue
        parsed_data = parse_game(parsed_data, game)
    return parsed_data


def sum_possible_ids(game_possible_dict: dict[int, bool]) -> int:
    possible_id_sum: int = 0
    for game_id, possible in game_possible_dict.items():
        if possible:
            possible_id_sum += game_id
    return possible_id_sum


def check_game_possible(game_data: dict, available_cubes: dict) -> bool:
    for hand in game_data:
        for colour, number in hand.items():
            if number > available_cubes[colour]:
                return False
    return True


def find_possible_games(parsed_data: dict, available_cubes: dict) -> dict:
    possible_game_dict = {}
    for game_id, game_data in parsed_data.items():
        # Loop through each game and check if there were enough cubes for each hand
        possible_game_dict[game_id] = check_game_possible(game_data, available_cubes)
    return possible_game_dict


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data: list = f_obj.read().split("\n")
    parsed_data: dict = parse_data(data)
    print(f"parsed_data: {parsed_data}")

    available_cubes: dict = {"red": 12, "green": 13, "blue": 14}
    # Loop through each game, and check if each hand was possible

    # Game #, true/false
    possible_game_dict: dict[int, bool] = find_possible_games(
        parsed_data, available_cubes
    )

    return sum_possible_ids(possible_game_dict)


def get_game_fewest_cubes(game_data: list) -> dict:
    current_highest: dict = defaultdict(lambda: 0)
    for hand in game_data:
        for colour, number in hand.items():
            if number > current_highest[colour]:
                current_highest[colour] = number
    return current_highest


def find_fewest_cubes_per_game(parsed_data: dict) -> dict:
    fewest_cubes = {}
    for game_id, game_data in parsed_data.items():
        fewest_cubes[game_id] = get_game_fewest_cubes(game_data)
    return fewest_cubes


def power_values(values: list) -> int:
    total_value: int = 0
    for value in values:
        if total_value == 0:
            total_value = value
            continue
        total_value *= value
    return total_value


def sum_power_of_cubes(fewest_cubes: dict) -> int:
    total_sum = 0
    for game_id, cubes in fewest_cubes.items():
        game_value: int = power_values(cubes.values())
        total_sum += game_value
    return total_sum


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = f_obj.read().split("\n")
    print(data)
    # Find the fewest possible cubes in each game
    parsed_data: dict = parse_data(data)
    fewest_cubes: dict = find_fewest_cubes_per_game(parsed_data)
    # sum the power of their cubes
    return sum_power_of_cubes(fewest_cubes)


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    print(part2(f"{current_day}/part2_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))
