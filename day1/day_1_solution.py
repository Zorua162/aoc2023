import re

regex = r"[a-z]"
number_words_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def part1(data_path: str):
    with open(data_path, "r") as f_obj:
        data = f_obj.read().split("\n")
    result = [re.sub(regex, "", line, 0) for line in data]
    print(result)
    numbers = [line[0] + line[-1] for line in result if line != ""]
    output = sum([int(number) for number in numbers])
    return output


def replace_words(data: list) -> list:
    out = []
    for line in data:
        current_line = line
        for word, value in number_words_dict.items():
            print(word, value)
            current_line = current_line.replace(word, value)
        out.append(current_line)
    return out


def part2(data_path: str):
    with open(data_path, "r") as f_obj:
        data = f_obj.read().split("\n")
    # replace all words that are numbers with their number
    data = replace_words(data)
    print(f"words replaced data {data}")

    result = [re.sub(regex, "", line, 0) for line in data]
    print(f"regex result {result}")
    numbers = [line[0] + line[-1] for line in result if line != ""]
    output = sum([int(number) for number in numbers])
    return output


if __name__ == "__main__":
    # print(part1("example_data.txt"))
    # print(part1("data.txt"))
    print(part2("example_data_part2.txt"))
    # print(part2("data.txt"))
