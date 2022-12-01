from pathlib import Path

INPUTS_DIR = Path(__file__).parent.parent / "inputs"


def get_input_lines(path_to_file: Path):
    input_lines = []
    with open(path_to_file, "r") as f:
        input_lines = [line.strip() for line in f.readlines()]
    return input_lines
