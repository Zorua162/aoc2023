from day11.day11_solution import part1, part2

current_day = "day11"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 374 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 9686930 == output


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part1_example_data.txt")
    assert 82000210 == output


def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert 630728425490 == output
