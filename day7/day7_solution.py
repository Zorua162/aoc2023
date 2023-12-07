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
                if 2 in string_data[2].values():
                    kinds_dict["full"].append(string_data)
                else:
                    kinds_dict["three"].append(string_data)

            # two
            case 2:
                if 1 in string_data[2].values():
                    raise Exception(
                        "This incorrectly determines when a two pair is "
                        "instead of a one pair is, for example 32T3K 765"
                    )
                    kinds_dict["two_pair"].append(string_data)
                else:
                    kinds_dict["one_pair"].append(string_data)
            # high
            case 1:
                kinds_dict["high"].append(string_data)
    return kinds_dict


def rank_bets(kinds: dict[str, list]) -> list:
    keys = ["five", "four", "full", "three", "two_pair", "one_pair", "high"]
    out_bets = []
    for key in keys:
        print(key)
        current_list = kinds[key]
        # Sort the hand
        sorted_hand = sorted(current_list, key=lambda x: x[0])
        out_bets.extend([int(hand[1]) for hand in sorted_hand])
    return out_bets


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line.split(" ") for line in f_obj.read().split("\n") if line != ""]
    print(data)
    # Sort into "kinds"
    counted_strings = count_string_occurrences(data)
    kinds = sort_into_kinds(counted_strings)
    print(kinds)
    ranked_bets = rank_bets(kinds)
    print(ranked_bets)
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
