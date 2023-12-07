from collections import defaultdict

current_day = "day7"


def count_string_occurrences(split_data: list[list]) -> list[list]:
    counted_strings = []
    for line in split_data:
        letter_dict: dict = defaultdict(lambda: 0)
        for letter in line[0]:
            letter_dict[letter] += 1
        line.append(letter_dict)
        counted_strings.append(line)
    return counted_strings


def convert_to_num(string: str) -> int:
    """Convert to number, where numbers have a large value then letters"""
    total_val = 0
    for i, char in enumerate(string):
        if char.isdigit():
            total_val += 10**i * (ord("a") + ord(char))
        else:
            total_val += 10**i * ord(char)
    return total_val


def get_adjusted_value_of_string(counted_strings: list[list]) -> list[list]:
    adjusted_value_lists = []
    for string_data in counted_strings:
        string_data.append(convert_to_num(string_data[0]))
        adjusted_value_lists.append(string_data)
    return adjusted_value_lists


def sort_into_kinds(counted_strings: list[list]) -> dict[str, list]:
    kinds_dict: dict[str, list] = defaultdict(lambda: [])
    for string_data in counted_strings:
        match max(string_data[2].values()):
            # five
            case 5:
                kinds_dict["five"].append(string_data)
            # four
            case 4:
                kinds_dict["four"].append(string_data)

            # full house / three
            case 3:
                if len(string_data[2].values()) == 2:
                    kinds_dict["full"].append(string_data)
                else:
                    kinds_dict["three"].append(string_data)

            # two
            case 2:
                if len(string_data[2].values()) == 3:
                    kinds_dict["two_pair"].append(string_data)
                else:
                    kinds_dict["one_pair"].append(string_data)
            # high
            case 1:
                kinds_dict["high"].append(string_data)
    return kinds_dict


def rank_bets(kinds: dict[str, list]) -> list:
    keys = ["five", "four", "full", "three", "two_pair", "one_pair", "high"]
    out_bets: list = []
    for key in keys:
        current_list = kinds[key]
        # Sort the hand
        sorted_values = sorted(current_list, key=lambda x: x[3])
        out_bets.extend([int(hand[1]) for hand in sorted_values])
        print(f"key {key} out_bets {out_bets}, current_list {current_list}")
    return out_bets


def calc_values(ranked_bets: list[int]) -> list[int]:
    return [(i + 1) * val for i, val in enumerate(reversed(ranked_bets))]


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line.split(" ") for line in f_obj.read().split("\n") if line != ""]
    # Sort into "kinds"
    counted_strings = count_string_occurrences(data)
    print(f"counted_strings {counted_strings}")
    adjusted = get_adjusted_value_of_string(counted_strings)
    print(f"\n adjusted {adjusted}")
    kinds = sort_into_kinds(adjusted)
    print(f"\nkinds {kinds}")
    ranked_bets = rank_bets(kinds)
    print(f"ranked_bets {ranked_bets}")
    values = calc_values(ranked_bets)

    return sum(values)


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
# 253774472 too high
