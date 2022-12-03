from aoclib import input_parsers

priorities = {chr(ord("a") + i): i + 1 for i in range(26)}
priorities.update({chr(ord("A") + i): 26 + i + 1 for i in range(26)})


def solve_part_one(input_file):
    rucksacks = input_parsers.get_input_lines(input_file)
    priorities_duplicates = 0
    for rucksack in rucksacks:
        size = len(rucksack)
        left = rucksack[: size // 2]
        right = rucksack[size // 2 :]
        duplicates = set(left).intersection(set(right))
        priorities_duplicates += sum(priorities[elem] for elem in duplicates)
    return priorities_duplicates


def solve_part_two(input_file):
    rucksacks = input_parsers.get_input_lines(input_file)
    priorities_badges = 0
    for i_group in range(len(rucksacks) // 3):
        badge = (
            set(rucksacks[i_group * 3])
            .intersection(set(rucksacks[i_group * 3 + 1]))
            .intersection(set(rucksacks[i_group * 3 + 2]))
        ).pop()
        priorities_badges += priorities[badge]
    return priorities_badges


if __name__ == "__main__":
    input_files = [
        input_parsers.INPUTS_DIR / file for file in ["03_test_input", "03_input"]
    ]
    for file in input_files:
        print(f"\t{file.name:=^20}")
        print(f"\t{solve_part_one(file)}")
        print(f"\t{solve_part_two(file)}")
