from day_x import main


def test_data_output():
    output = main("data.txt")
    assert output == ["1", "2", "3", "4", "5", "6", ""]


def test_example_data_output():
    output = main("data.txt")
    assert output == ["1", "2", "3", ""]
