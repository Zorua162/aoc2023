from itertools import combinations

current_day = "day11"


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def print_to_file(data: list[str]):
    with open(f"{current_day}/printed.txt", "w") as f_out:
        for line in data:
            f_out.write("".join(line) + "\n")


def transpose(M):
    return [
        "".join(row)
        for row in [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    ]


def expand_universe(data: list[str]) -> list[str]:
    """For every row and column which doesn't have a # add another "empty" row of ."""
    empty_row = "." * len(data[0])
    expanded_vertically = []
    for row in data:
        if row == empty_row:
            expanded_vertically.append(empty_row)
        expanded_vertically.append(row)

    # Transpose to make expanding easier
    transposed = transpose(expanded_vertically)

    transposed_expanded = []

    empty_horizontal = "." * len(transposed[0])
    for row in transposed:
        if row == empty_horizontal:
            transposed_expanded.append(empty_horizontal)
        transposed_expanded.append(row)

    return transpose(transposed_expanded)


def assign_numbers(data: list[str]) -> tuple[list[str], int]:
    current = 1
    out_data = []
    for j, row in enumerate(data):
        new_row = []
        for i, char in enumerate(row):
            if char == "#":
                new_row.append(str(current))
                current += 1
            else:
                new_row.append(".")
        out_data.append(new_row)
    return out_data, current - 1


def get_location(data: list[str], num: int) -> tuple[int, int]:
    for j, row in enumerate(data):
        for i, val in enumerate(row):
            if val == str(num):
                return i, j
    return None


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_location(self) -> tuple[int, int]:
        return self.x, self.y


def create_points(data: list[str], highest: int) -> list[Point]:
    points = []
    for i in range(1, highest + 1):
        x, y = get_location(data, i)
        points.append(Point(x, y))
    return points


def count_distances(data: list[str], highest: int) -> int:
    distance = 0

    # for pair in combinations(range(1, highest + 1), 2):
    #     print(pair)
    #     x1, y1 = get_location(data, pair[0])
    #     x2, y2 = get_location(data, pair[1])
    #     distance += abs(x1 - x2)
    #     distance += abs(y1 - y2)

    points = create_points(data, highest)

    for pair in combinations(points, 2):
        print(pair)
        x1, y1 = pair[0].get_location()
        x2, y2 = pair[1].get_location()
        distance += abs(x1 - x2)
        distance += abs(y1 - y2)

    return distance


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    data = expand_universe(data)
    data, highest = assign_numbers(data)
    print_to_file(data)
    print_grid(data)
    print(highest)

    distance = count_distances(data, highest)
    return distance


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print_grid(data)
    return 0


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data.txt"))
    # print(part2(f"{current_day}/data.txt"))
