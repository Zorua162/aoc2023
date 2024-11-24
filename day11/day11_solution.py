from itertools import combinations

current_day = "day11"


class Point:
    x: int
    y: int
    expanded_x: int
    expanded_y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.expanded_x = x
        self.expanded_y = y

    def get_location(self) -> tuple[int, int]:
        return self.x, self.y

    def get_expanded(self) -> tuple[int, int]:
        return self.expanded_x, self.expanded_y


class Expanse:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


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


def expand_universe(data: list[str], amount: int = 1) -> list[str]:
    """For every row and column which doesn't have a # add another "empty" row of ."""
    print("Started vertical")
    empty_row = "." * len(data[0])
    expanded_vertically = []
    for row in data:
        if row == empty_row:
            for i in range(amount):
                if i % 10000 == 0:
                    print(f"On row {i}")
                expanded_vertically.append(empty_row)
        expanded_vertically.append(row)

    print("Transposing")
    # Transpose to make expanding easier
    transposed = transpose(expanded_vertically)

    transposed_expanded = []

    print("Started horizontal")
    empty_horizontal = "." * len(transposed[0])
    for row in transposed:
        if row == empty_horizontal:
            for i in range(amount):
                if i % 10000 == 0:
                    print(f"On row {i}")
                transposed_expanded.append(empty_horizontal)
        transposed_expanded.append(row)
    print("Transposing back")

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


def create_points(data: list[str], highest: int) -> list[Point]:
    points = []
    for i in range(1, highest + 1):
        print(i)
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


def create_expanses(data: list[str]) -> list[Expanse]:
    expanses = []
    empty_row = ["."] * len(data[0])

    for j, row in enumerate(data):
        print(row)
        if row == empty_row:
            expanses.append(Expanse(None, j))

    for i in range(len(data[0])):
        for row in data:
            if row[i] != ".":
                break
        else:
            expanses.append(Expanse(i, None))

    return expanses


def calculate_distances(points: list[Point]) -> int:
    distance = 0
    for pair in combinations(points, 2):
        x1, y1 = pair[0].get_expanded()
        print(f"{x1}, {y1}")
        x2, y2 = pair[1].get_expanded()
        distance += abs(x1 - x2)
        distance += abs(y1 - y2)

    return distance


def part2(data_path: str) -> int:
    expand_by = 1000000
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    data, highest = assign_numbers(data)
    points = create_points(data, highest)

    expanses = create_expanses(data)

    # Adjust the x and y positions based on the expanded universe
    for expanse in expanses:
        print(f"{expanse.x}, {expanse.y}")
        for point in points:
            if expanse.x is not None and point.x > expanse.x:
                print("expanded_point")
                point.expanded_x += expand_by - 1
                print(point.expanded_x)
            if expanse.y is not None and point.y > expanse.y:
                point.expanded_y += expand_by - 1

    print("Points")
    for i, point in enumerate(points):
        print(f"{i+1}: {point.expanded_x}, {point.expanded_y}")

    distance = calculate_distances(points)

    return distance


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part1_example_data.txt"))
    print(part2(f"{current_day}/data.txt"))

# 82000210 - Too low
