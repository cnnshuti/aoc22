from aoclib import input_parsers
from pathlib import Path


def calories_lists(input_file: Path):
    input_lines = input_parsers.get_input_lines(input_file)
    result = []
    curr_elf_calories = []
    for line in input_lines:
        if len(line) == 0:
            result.append(curr_elf_calories[:])
            curr_elf_calories = []
            continue
        curr_elf_calories.append(int(line))
    result.append(curr_elf_calories[:])
    return result


def solve_part_one(input_file: Path):
    return max(sum(calories_list) for calories_list in calories_lists(input_file))


def solve_part_two(input_file: Path):
    return sum(
        sorted(sum(calories_list) for calories_list in calories_lists(input_file))[-3:]
    )


if __name__ == "__main__":
    input_files = [
        input_parsers.INPUTS_DIR / file for file in ["01_test_input", "01_input"]
    ]
    for file in input_files:
        print(f"\t{file.name:=^20}")
        print(f"\t{solve_part_one(file)}")
        print(f"\t{solve_part_two(file)}")
