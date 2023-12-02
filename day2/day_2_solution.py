def part1(data_path):
    with open(data_path, "r") as f_obj:
        data = f_obj.read().split("\n")
    print(data)
    return data


def part2(data_path):
    with open(data_path, "r") as f_obj:
        data = f_obj.read().split("\n")
    print(data)
    return data


if __name__ == "__main__":
    part1("part1_example_data.txt")
    # part1("data.txt")
    # part2("part2_example_data.txt")
    # part2("data.txt")
