from aoclib import input_parsers
from collections import defaultdict

def find_marker(line, marker_length):
    num_distinct_characters = 0
    marker_candidate = defaultdict(int)
    for i in range(len(line)):
        # print(i, num_distinct_characters, marker_candidate)
        c = line[i]
        marker_candidate[c] += 1
        if marker_candidate[c] == 1:
            num_distinct_characters += 1
        if i < marker_length-1:
            continue
        if num_distinct_characters == marker_length:
            return i+1, line[i-(marker_length-1):i+1]
        else:
            marker_candidate[line[i - (marker_length-1)]] -= 1
            if marker_candidate[line[i - (marker_length-1)]] == 0:
                num_distinct_characters -= 1
    return None

def solve_part_one(input_file):
    for i, line in enumerate(input_parsers.get_input_lines(input_file)):
        print(i, find_marker(line, 4))


def solve_part_two(input_file):
    for i, line in enumerate(input_parsers.get_input_lines(input_file)):
        print(i, find_marker(line, 14))

if __name__ == "__main__":
    input_files = [
        input_parsers.INPUTS_DIR / file for file in ["06_test_input", "06_input"]
    ]
    for file in input_files:
        print(f"\t{file.name:=^20}")
        print(f"\t{solve_part_one(file)}")
        print(f"\t{solve_part_two(file)}")
