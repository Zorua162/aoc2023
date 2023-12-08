from collections import defaultdict

from day7.day7_solution_part1 import (
    count_string_occurrences,
    rank_bets,
    calc_values,
)

current_day = "day7"
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
priority_dict = {
    character: value for value, character in enumerate(reversed(priority_list_part_2))
}


def handle_jokers(string_data: list) -> list:
    """Determine the best hand with this string, which contains a Joker in it"""
    print("handle_jokers called")
    counted_cards: dict[str, int] = string_data[2]
    max_card = [
        key
        for key, value in counted_cards.items()
        if value == max(counted_cards.values())
    ][0]
    counted_cards[max_card] += counted_cards["J"]
    counted_cards["J"] = 0
    string_data[2] = counted_cards
    return string_data


def sort_into_kinds(counted_strings: list[list]) -> dict[str, list]:
    kinds_dict: dict[str, list] = defaultdict(lambda: [])
    for string_data in counted_strings:
        if "J" in string_data[0]:
            string_data = handle_jokers(string_data)

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


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line.split(" ") for line in f_obj.read().split("\n") if line != ""]
    # Sort into "kinds"
    counted_strings = count_string_occurrences(data)
    print(f"counted_strings {counted_strings}")
    print(f"\n adjusted {counted_strings}")
    kinds = sort_into_kinds(counted_strings)
    print(f"\nkinds {kinds}")
    ranked_bets = rank_bets(kinds)
    print(f"ranked_bets {ranked_bets}")
    values = calc_values(ranked_bets)

    return sum(values)


if __name__ == "__main__":
    # print(part2(f"{current_day}/part2_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# Submitted answers
# 254272195 too high
