import shutil
import os


def create_folder(day_number: int) -> None:
    # Copy the folder
    shutil.copytree("template", f"day{day_number}")


def change_file_names(day_number: int) -> None:
    day_folder = f"day{day_number}"
    # Renmae the solution file
    os.rename(
        f"{day_folder}/dayx_solution.py", f"{day_folder}/day{day_number}_solution.py"
    )
    # Rename the tests file
    os.rename(f"{day_folder}/test_dayx.py", f"{day_folder}/test_day{day_number}.py")


def update_file_content(day_number: int) -> None:
    day_folder = f"day{day_number}"
    file_list = [f"{day_folder}/day1_solution.py"]
    for file_name in file_list:
        with open(file_name, "w") as f_obj:
            file_content = f_obj.read()
            print(file_content)
            # replace the file name
            file_content.replace("dayx", f"day{day_number}")
            # replace the folder name
            file_content.replace("template", f"day{day_number}")
            f_obj.write(file_content)


def main():
    valid = False
    while not valid:
        try:
            day_number = int(input("Please input the day number:"))
        except ValueError:
            print("Invalid value, must be an integer")
            continue
        if day_number > 26:
            print("Day value too high, must be < 26")
            continue
        if day_number < 1:
            print("Day value too low, must be >= 1")
            continue
        valid = True
    print(f"Using day number {day_number}")
    create_folder(day_number)


if __name__ == "__main__":
    main()
