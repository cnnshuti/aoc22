from aoclib import input_parsers


def solve_part_one(input_file):
    lines = input_parsers.get_input_lines(input_file)
    fully_contained_assignments = 0
    for line in lines:
        pair1, pair2 = line.split(",")
        l1, r1 = (int(x) for x in pair1.split("-"))
        l2, r2 = (int(x) for x in pair2.split("-"))
        fully_contained_assignments += (l1 <= l2 and r1 >= r2) or (
            l2 <= l1 and r2 >= r1
        )
    return fully_contained_assignments


def solve_part_two(input_file):
    lines = input_parsers.get_input_lines(input_file)
    overlapping_pairs = 0
    for line in lines:
        pair1, pair2 = line.split(",")
        l1, r1 = (int(x) for x in pair1.split("-"))
        l2, r2 = (int(x) for x in pair2.split("-"))
        overlapping_pairs += max((l1, r1), (l2, r2))[0] <= min((l1, r1), (l2, r2))[1]
    return overlapping_pairs


if __name__ == "__main__":
    input_files = [
        input_parsers.INPUTS_DIR / file for file in ["04_test_input", "04_input"]
    ]
    for file in input_files:
        print(f"\t{file.name:=^20}")
        print(f"\t{solve_part_one(file)}")
        print(f"\t{solve_part_two(file)}")
