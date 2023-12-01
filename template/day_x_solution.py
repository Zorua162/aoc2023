def main(data_path):
    with open(data_path, "r") as f_obj:
        data = f_obj.read().split("\n")
    print(data)
    return data


if __name__ == "__main__":
    main("data.txt")
    main("example_data.txt")
