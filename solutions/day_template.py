from aoclib import input_parsers


def solve_part_one(input_file):
    return None


def solve_part_two(input_file):
    return None


if __name__ == "__main__":
    input_files = [
        input_parsers.INPUTS_DIR / file for file in ["04_test_input", "04_input"]
    ]
    for file in input_files:
        print(f"\t{file.name:=^20}")
        print(f"\t{solve_part_one(file)}")
        print(f"\t{solve_part_two(file)}")
