from aoclib import input_parsers
from copy import deepcopy

def get_crates_and_moves(input_lines):
    crates_lines = []
    moves_lines = []
    for i in range(len(input_lines)):
        if input_lines[i].startswith('move'):
            crates_lines = input_lines[:i-1]
            moves_lines = input_lines[i:]
            break
    crates = {
        int(crate_name.strip()): []
        for crate_name in crates_lines[-1].split('  ')
    }
    for i in range(len(crates_lines)-2, -1,-1):
        for ielem in range(len(crates)):
            elem = crates_lines[i][ielem*4+1]
            if len(elem.strip()) > 0:
                crates[ielem+1].append(elem)
    
    moves = []
    for line in moves_lines:
        elements = line.split(' ')
        moves.append((int(elements[1]), int(elements[3]), int(elements[5])))
    return crates, moves


def solve_part_one(input_file):
    crates, moves = get_crates_and_moves(input_parsers.get_input_lines(input_file, no_strip=True))
    crates_, moves_ = deepcopy(crates), deepcopy(moves)
    for move in moves:
        n, src, to = move
        for _ in range(n):
            crates_[to].append(crates_[src].pop())
    on_top = ''.join([crates_[i+1][-1] for i in range(len(crates_))])
    return on_top


def solve_part_two(input_file):
    crates, moves = get_crates_and_moves(input_parsers.get_input_lines(input_file, no_strip=True))
    crates_, moves_ = deepcopy(crates), deepcopy(moves)
    for move in moves:
        n, src, to = move
        crates_[to] += crates_[src][-n:]
        crates_[src][-n:] = []
    on_top = ''.join([crates_[i+1][-1] for i in range(len(crates_))])
    return on_top

if __name__ == "__main__":
    input_files = [
        input_parsers.INPUTS_DIR / file for file in ["05_test_input", "05_input"]
    ]
    for file in input_files:
        print(f"\t{file.name:=^20}")
        print(f"\t{solve_part_one(file)}")
        print(f"\t{solve_part_two(file)}")
