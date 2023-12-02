import shutil
import os


def create_folder(day_number: int) -> None:
    # Copy the folder
    print("Copying files into folder")
    try:
        shutil.copytree("template", f"day{day_number}")
    except FileExistsError:
        raise Exception(f"Folder day{day_number} already exists, exiting")


def change_file_names(day_number: int) -> None:
    print("Updating file names")
    day_folder = f"day{day_number}"
    # Renmae the solution file
    os.rename(
        f"{day_folder}/dayx_solution.py", f"{day_folder}/day{day_number}_solution.py"
    )
    # Rename the tests file
    os.rename(f"{day_folder}/test_dayx.py", f"{day_folder}/test_day{day_number}.py")


def update_file_content(day_number: int) -> None:
    print("Editing files")
    day_folder = f"day{day_number}"
    file_list = [
        f"{day_folder}/day{day_number}_solution.py",
        f"{day_folder}/test_day{day_number}.py",
    ]
    for file_name in file_list:
        print(f"    Currently editing {file_name}")
        with open(file_name, "r") as read_obj:
            file_content = read_obj.read()
        # print(file_content)
        # replace the file name
        file_content = file_content.replace("dayx", f"day{day_number}")
        # replace the folder name
        file_content = file_content.replace("template", f"day{day_number}")
        with open(file_name, "w") as write_obj:
            write_obj.write(file_content)


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
    change_file_names(day_number)
    update_file_content(day_number)


if __name__ == "__main__":
    main()
