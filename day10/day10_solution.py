from __future__ import annotations

current_day = "day10"
directions = {
    "north": (0, -1),
    "east": (1, 0),
    "south": (0, 1),
    "west": (-1, 0),
}

connects_to = {
    "north": ["|", "7", "F"],
    "east": ["-", "J", "7"],
    "south": ["|", "L", "J"],
    "west": ["-", "L", "F"],
}

translate_direction = {
    "west": "east",
    "east": "west",
    "north": "south",
    "south": "north",
}

find_outgoing = {
    "L": {"north": "east", "east": "north"},
    "|": {"north": "south", "south": "north"},
    "-": {"east": "west", "west": "east"},
    "J": {"north": "west", "west": "north"},
    "7": {"south": "west", "west": "south"},
    "F": {"south": "east", "east": "south"},
}

find_inner_side = {
    "|": {"north": ["west"], "south": ["east"]},
    "-": {"east": ["north"], "west": ["south"]},
    "L": {"north": ["south", "west"], "east": []},
    "J": {"north": [], "west": ["south", "east"]},
    "7": {"south": ["north", "east"], "west": []},
    "F": {"south": [], "east": ["north", "west"]},
    "S": {"north": [], "south": [], "east": [], "west": []},
}


class Pipe:
    x: int
    y: int
    type: str
    distance: int
    # last_pipe: "Pipe"
    last_pipe: Pipe
    incoming_direction: str

    def __init__(
        self,
        x: int,
        y: int,
        type: str,
        distance: int,
        last_pipe: Pipe,
        incoming_direction: str,
    ):
        self.x = x
        self.y = y
        self.type = type
        self.distance = distance
        self.last_pipe = last_pipe
        self.incoming_direction = incoming_direction

    def find_starting_pipes(self, data: list[str]) -> list[Pipe]:
        # Look at all 4 locations around the pipe

        pipes = []
        for direction in directions.keys():
            pipe = self.check_dir(direction, data)
            if pipe is not None:
                pipes.append(pipe)
        return pipes

    def check_dir(self, direction, data: list[str]):
        dx = directions[direction][0]
        dy = directions[direction][1]
        try:
            loc = data[self.y + dy][self.x + dx]
        except IndexError:
            print("Index error")
            return
        if loc in connects_to[direction]:
            return Pipe(
                self.x + dx,
                self.y + dy,
                loc,
                self.distance + 1,
                self,
                translate_direction[direction],
            )
        return None

    def find_next(self, data) -> Pipe:
        """Based on last pipe and current type find the coordinates of the next pipe"""
        outgoing_direction = find_outgoing[self.type][self.incoming_direction]
        dx = directions[outgoing_direction][0]
        dy = directions[outgoing_direction][1]
        next_x = self.x + dx
        next_y = self.y + dy
        return Pipe(
            next_x,
            next_y,
            data[next_y][next_x],
            self.distance + 1,
            self,
            translate_direction[outgoing_direction],
        )


def print_grid(grid: list[str]):
    for line in grid:
        print(line)


def find_all_pipes(data: list[str], current_pipe: Pipe) -> list[Pipe]:
    pipe_list = [current_pipe]
    while current_pipe.type != "S":
        current_pipe = current_pipe.find_next(data)
        print(current_pipe.type, current_pipe.distance)
        pipe_list.append(current_pipe)
    return pipe_list


def get_all_pipes(data: list[str]) -> list[Pipe]:
    # Find the start location
    for i, line in enumerate(data):
        for j, loc in enumerate(line):
            if loc == "S":
                start_pipe = Pipe(j, i, "S", 0, None, None)
                pipes = start_pipe.find_starting_pipes(data)

    all_pipes = find_all_pipes(data, pipes[0])
    print(all_pipes)
    return all_pipes


def part1(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]

    all_pipes = get_all_pipes(data)

    return len(all_pipes) / 2


def fill_around(grid: list[str], x: int, y: int) -> list[str]:
    """Fill the given location and all adjacent spaces with a dot (.)"""
    grid[y][x] = "x"
    for direction in directions.values():
        new_x = x + direction[0]
        new_y = y + direction[1]
        if grid[new_y][new_x] == ".":
            fill_around(grid, new_x, new_y)

    return grid


def fill_inner(grid: list[str], all_pipes: list[Pipe]) -> list[str]:
    """Fill the inner sections with x"""
    for pipe in all_pipes:
        inner_sides = find_inner_side[pipe.type][pipe.incoming_direction]
        print(pipe.type, inner_sides)
        for side in inner_sides:
            direction = directions[side]
            x = pipe.x + direction[0]
            y = pipe.y + direction[1]
            if grid[y][x] == ".":
                grid = fill_around(grid, x, y)

    return grid


def count_xs(grid: list[str]) -> int:
    count = 0
    for line in grid:
        for i in line:
            if i == "x":
                count += 1
    return count


def part2(data_path: str) -> int:
    with open(data_path, "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    all_pipes = get_all_pipes(data)

    # Plan
    # Replace each pipe with a #
    # replace everything else with a .
    # Loop through each pipe and on the "right" of it, flood fill all . with x
    # Count the number of x to get our output

    grid = [["."] * len(data[0]) for line in data]

    for pipe in all_pipes:
        grid[pipe.y][pipe.x] = "#"

    fill_inner(grid, all_pipes)
    print(grid)

    with open(f"{current_day}/grid.txt", "w") as f_out:
        for line in grid:
            out_line = "".join(line) + "\n"
            print(out_line)
            f_out.write(out_line)

    return count_xs(grid)


if __name__ == "__main__":
    # print(part1(f"{current_day}/part1_example_data.txt"))
    # print(part1(f"{current_day}/data.txt"))
    # print(part2(f"{current_day}/part2_example_data_2.txt"))
    print(part2(f"{current_day}/data.txt"))

# 249 too low - Likely due to needing to flood fill!
