from collections import defaultdict
import json

from functools import cmp_to_key

current_day = "day7"
priority_list_part_1 = [
    "A",
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "1",
]
priority_list_part_2 = [
    "A",
    "K",
    "Q",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "1",
    "J",
]


def count_string_occurrences(split_data: list[list]) -> list[list]:
    counted_strings = []
    for line in split_data:
        letter_dict: dict = defaultdict(lambda: 0)
        for letter in line[0]:
            letter_dict[letter] += 1
        line.append(letter_dict)
        counted_strings.append(line)
    return counted_strings


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


def comp_strings(a: str, b: str, priority_dict) -> int:
    # print(f"comp_strings {a} {b}")
    a_characters = a[0]
    b_characters = b[0]
    for i in range(len(a_characters)):
        if a_characters[i] == b_characters[i]:
            continue
        return round(
            2
            * ((priority_dict[a_characters[i]] < priority_dict[b_characters[i]]) - 0.5)
        )
    return 0


def sort_values(values: list, priority_dict: dict) -> list:
    return sorted(
        values,
        key=cmp_to_key(lambda a, b: comp_strings(a, b, priority_dict)),  # type: ignore
    )
    # return sorted(values, key=lambda x: priority_dict[x[0]])


def create_priority_dict(priority_list: list) -> dict:
    return {character: value for value, character in enumerate(reversed(priority_list))}


def rank_bets(kinds: dict[str, list], priority_list) -> list:
    keys = ["five", "four", "full", "three", "two_pair", "one_pair", "high"]
    priority_dict = create_priority_dict(priority_list)
    out_bets: list = []
    for key in keys:
        current_list = kinds[key]
        # Sort the hand
        out_bets.extend(
            [int(hand[1]) for hand in sort_values(current_list, priority_dict)]
        )
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
    print(f"\n adjusted {counted_strings}")
    kinds = sort_into_kinds(counted_strings)
    print(f"\nkinds {kinds}")
    ranked_bets = rank_bets(kinds, priority_list_part_1)
    print(f"ranked_bets {ranked_bets}")
    values = calc_values(ranked_bets)

    return sum(values)


def handle_jokers(counted_strings: list) -> list:
    """Determine the best hand with this string, which contains a Joker in it"""
    for i, string_data in enumerate(counted_strings):
        if "J" in string_data[0]:
            counted_cards: dict[str, int] = string_data[2]
            print(f"counted_cards_pre pre {counted_cards}")
            counted_cards_no_j = counted_cards.copy()
            if len(counted_cards_no_j) > 1:
                print("J removed")
                del counted_cards_no_j["J"]
                print(f"counted_cards_no_j {counted_cards_no_j}")
            max_card = [
                key
                for key, value in counted_cards_no_j.items()
                if value == max(counted_cards_no_j.values())
            ][0]
            print(f"counted card pre add {counted_cards} max_card {max_card}")
            counted_cards[max_card] += counted_cards["J"]
            print(f"counted card post add {counted_cards}")
            counted_cards["J"] = 0
            string_data[2] = counted_cards
            counted_strings[i] = string_data

    return counted_strings


def write_out_to_file(kinds: dict) -> None:
    for key in kinds:
        with open(f"{current_day}/kinds_{key}.txt", "w") as out_obj:
            json.dump(kinds[key], out_obj, indent=4)


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line.split(" ") for line in f_obj.read().split("\n") if line != ""]
    # Sort into "kinds"
    counted_strings = count_string_occurrences(data)
    print(f"counted_strings {counted_strings}")
    counted_strings = handle_jokers(counted_strings)
    print(f"\n jokers handled{counted_strings}")
    kinds = sort_into_kinds(counted_strings)
    print(f"\nkinds {kinds}")
    write_out_to_file(kinds)
    ranked_bets = rank_bets(kinds, priority_list_part_2)
    print(f"ranked_bets {ranked_bets}")
    values = calc_values(ranked_bets)

    return sum(values)


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# Submitted answers
# 253774472 too high
# 252540485 too low
# 253511455 too high
