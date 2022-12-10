from aoclib import input_parsers


def solve_part_one(input_file):
    instructions = input_parsers.get_input_lines(input_file)
    i_instr = -1
    cycle = 1
    x = 1
    instr_cycle = 0 
    res = 0
    while cycle < 1_000_000:
        if instr_cycle == 0:
            i_instr += 1
            if i_instr >= len(instructions):
                break
            instr_cycle = 2 if instructions[i_instr].startswith('addx') else 1
        if (cycle - 20) % 40 == 0:
            res += cycle * x
        
        # apply instruction
        instr_cycle -= 1
        if (instructions[i_instr].startswith('addx')
            and instr_cycle == 0):
            x += int(instructions[i_instr][5:])
        cycle += 1
    return res


def solve_part_two(input_file):
    instructions = input_parsers.get_input_lines(input_file)
    i_instr = -1
    cycle = 1
    x = 1
    instr_cycle = 0 
    res = 0
    while cycle < 1_000_000:
        if abs(((cycle-1) %40) - x) <= 1:
            print('#', end='')
        else:
            print('.', end='')
        if instr_cycle == 0:
            i_instr += 1
            if i_instr >= len(instructions):
                break
            instr_cycle = 2 if instructions[i_instr].startswith('addx') else 1
        if (cycle - 20) % 40 == 0:
            res += cycle * x
        
        # apply instruction
        instr_cycle -= 1
        if (instructions[i_instr].startswith('addx')
            and instr_cycle == 0):
            x += int(instructions[i_instr][5:])
        
        cycle += 1
        if (cycle-1) % 40 == 0:
            print('\n',end='')
    return res


if __name__ == "__main__":
    input_files = [
        input_parsers.INPUTS_DIR / file for file in ["10_test_input", "10_input"]
    ]
    for file in input_files:
        print(f"\t{file.name:=^20}")
        print(f"\t{solve_part_one(file)}")
        print(f"\t{solve_part_two(file)}")
