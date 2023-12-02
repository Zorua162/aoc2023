current_day = "dayx"


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
    print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
