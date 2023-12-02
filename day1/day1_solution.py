import re

regex = r"[a-z]"
number_words_dict: dict[str, str] = {
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


def build_index(data: list) -> list[dict]:
    """Build and index which has format:
    location of first character: number"""
    index: list[dict] = []
    for line in data:
        line_index: dict = {}
        for word, value in number_words_dict.items():
            # Find all the words for the numbers
            word_indexes = re.finditer(word, line)
            for word_index in word_indexes:
                line_index[word_index.start()] = value
            # Find all the numebers
            value_indexes = re.finditer(value, line)
            for value_index in value_indexes:
                line_index[value_index.start()] = value
        index.append(line_index)
    return index


def build_result(index_data: list[dict]) -> list:
    """Build the list of values from the index data"""
    out: list = []
    for line in index_data:
        line_out = ""
        for index in sorted(line.keys()):
            line_out += line[index]
        out.append(line_out)
    return out


def part2(data_path: str):
    with open(data_path, "r") as f_obj:
        data = f_obj.read().split("\n")
    # replace all words that are numbers with their number
    index_data: list[dict] = build_index(data)
    result: list = build_result(index_data)
    numbers = [line[0] + line[-1] for line in result if line != ""]
    output = sum([int(number) for number in numbers])
    return output


if __name__ == "__main__":
    # print(part1("example_data.txt"))
    # print(part1("data.txt"))
    print(part2("example_data_part2.txt"))
    print(part2("data.txt"))
