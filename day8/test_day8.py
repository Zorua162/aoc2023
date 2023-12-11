from day8.day8_solution import (
    part1,
    part2,
    parse_data,
    compute_instruction_paths,
    in_all_indexes,
    last_run_all_z_at_same_time,
)
import pytest

current_day = "day8"


@pytest.fixture
def example_data() -> list[str]:
    with open(f"{current_day}/part1_example_data.txt", "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print(data)
    return data


@pytest.fixture
def example_data_part_2() -> list[str]:
    with open(f"{current_day}/part2_example_data.txt", "r") as f_obj:
        data = [line for line in f_obj.read().split("\n") if line != ""]
    print(data)
    return data


def test_parse_data(example_data) -> None:
    parsed_data = parse_data(example_data)
    print(parsed_data)
    assert parsed_data[0] == "RL"
    assert parsed_data[1]["AAA"]["R"] == "CCC"


def test_part1_example_data_output() -> None:
    output: int = part1(f"{current_day}/part1_example_data.txt")
    assert 2 == output


def test_part1_example_data_output_2() -> None:
    output: int = part1(f"{current_day}/part1_example_data_2.txt")
    assert 6 == output


def test_part1_data_output():
    output = part1(f"{current_day}/data.txt")
    assert 19951 == output


def test_compute_instruction_paths(example_data_part_2) -> None:
    instructions, paths = parse_data(example_data_part_2)
    full_instruction_path_data = compute_instruction_paths(instructions, paths)
    print(full_instruction_path_data)
    assert "11Z" == full_instruction_path_data["11A"]["end_location"]
    assert "22C" == full_instruction_path_data["22A"]["end_location"]
    assert [1] == full_instruction_path_data["11A"]["z_indexes"]


def test_in_all_indexes() -> None:
    index = 1
    data_all_contain = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    assert in_all_indexes(index, data_all_contain)

    index_not_in = 4
    assert not in_all_indexes(index_not_in, data_all_contain)


def test_last_run_all_z_at_same_time() -> None:
    data = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    assert last_run_all_z_at_same_time(data, 10)[0]
    # Index -> step is + 1
    assert 2 == last_run_all_z_at_same_time(data, 1)[1]

    data_not_same = [[1], [2], [3]]
    assert not last_run_all_z_at_same_time(data_not_same, 10)[0]
    assert 10 == last_run_all_z_at_same_time(data_not_same, 10)[1]


def test_part2_example_data_output() -> None:
    output: int = part2(f"{current_day}/part2_example_data.txt")
    assert 6 == output


@pytest.mark.skip("Answer is from AOC website")
def test_part2_data_output():
    output = part2(f"{current_day}/data.txt")
    assert "currently unknown" == output
