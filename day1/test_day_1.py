from day1.day_1_solution import part1, part2, build_index, build_result


def test_example_data_output_part1():
    output = part1("example_data.txt")
    assert output == 142


def test_data_output_part1():
    output = part1("data.txt")
    assert output == 54390


def test_build_index():
    word_list = ["1one2two", "three3four4", "6fiveight"]
    out = build_index(word_list)
    print(out)
    assert [
        {1: "1", 0: "1", 5: "2", 4: "2"},
        {0: "3", 5: "3", 6: "4", 10: "4"},
        {1: "5", 0: "6", 4: "8"},
    ] == out


def test_build_result():
    index_data = [
        {1: "1", 0: "1", 5: "2", 4: "2"},
        {0: "3", 5: "3", 6: "4", 10: "4"},
        {1: "5", 0: "6", 4: "8"},
    ]
    out = build_result(index_data)
    assert ["1122", "3344", "658"] == out


def test_example_data_output_part2():
    output = part2("example_data_part2.txt")
    assert output == 281


def test_data_output_part2():
    output = part2("data.txt")
    assert output == 54277
