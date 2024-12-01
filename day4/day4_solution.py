current_day = "day4"


def parse_data(data: list) -> list:
    split_data = [line.split(": ")[1].split(" | ") for line in data]
    parsed_data = []
    for card in split_data:
        card_numbers = [number for number in card[0].split(" ") if number != ""]
        winning_numbers = [number for number in card[1].split(" ") if number != ""]
        parsed_data.append([card_numbers, winning_numbers])
    return parsed_data


def count_wins(card_numbers: list, winning_numbers: list) -> int:
    """Count the number of wins in the current card

    Args:
        card_numbers (list): The numbers on the card
        winning_numbers (list): The winning numbers

    Returns:
        int: The number of winning numbers
    """
    count = 0
    for number in card_numbers:
        if number in winning_numbers:
            count += 1
    return count


def calculate_value(card: list) -> int:
    total = 0
    card_numbers = card[0]
    winning_numbers = card[1]
    cards_wins = count_wins(card_numbers, winning_numbers)
    if cards_wins > 0:
        print(f"Card wins {cards_wins}")
        card_value = 2 ** (cards_wins - 1)
        print(f"Current card value: {card_value}")
        total += card_value
    return total


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    parsed_data = parse_data(data)
    print(parsed_data)
    total = 0
    for card in parsed_data:
        wins = calculate_value(card)
        total += wins

    return total


def check_line_wins(
    card_number: int, parsed_data: list, total_scratchcards: int
) -> int:
    """Check the number of wins in the caard

    Args:
        card_number (int): The card number
        data (list): The dataset

    Returns:
        int: Number of winning numbers
    """
    total_scratchcards += 1
    card = parsed_data[card_number - 1]
    number_of_wins = count_wins(card[0], card[1])
    for new_card_number in range(card_number + 1, card_number + number_of_wins + 1):
        # print(f"Starting check on card {new_card_number} from card {card_number}")
        total_scratchcards = check_line_wins(
            new_card_number, parsed_data, total_scratchcards
        )
    return total_scratchcards


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    parsed_data = parse_data(data)
    total_scratchcards = 0
    for i in range(1, len(parsed_data) + 1):
        print(f"Starting on card {i}")
        total_scratchcards = check_line_wins(i, parsed_data, total_scratchcards)
    return total_scratchcards


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))
