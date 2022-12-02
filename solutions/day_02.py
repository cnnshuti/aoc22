from aoclib import input_parsers
from enum import Enum


class RPC(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


opponent_mapping = {
    "A": RPC.ROCK,
    "B": RPC.PAPER,
    "C": RPC.SCISSORS,
}

player_mapping = {"X": RPC.ROCK, "Y": RPC.PAPER, "Z": RPC.SCISSORS}

defeats = {RPC.ROCK: RPC.SCISSORS, RPC.SCISSORS: RPC.PAPER, RPC.PAPER: RPC.ROCK}
defeated_by = {v: k for k, v in defeats.items()}

scores = {RPC.ROCK: 1, RPC.PAPER: 2, RPC.SCISSORS: 3}


def get_tournament_games(input_lines):
    return [line.split(" ") for line in input_lines]


def solve_part_one(input_file):
    tournament_games = get_tournament_games(input_parsers.get_input_lines(input_file))
    tourname_score = 0
    for game in tournament_games:
        opponent, player = game
        opponent, player = (opponent_mapping[opponent], player_mapping[player])
        result_score = 0
        if opponent == player:
            result_score = 3
        elif defeats[player] == opponent:
            result_score = 6
        tourname_score += result_score + scores[player]
    return tourname_score


def solve_part_two(input_file):
    tournament_games = get_tournament_games(input_parsers.get_input_lines(input_file))
    tourname_score = 0
    for game in tournament_games:
        opponent, target_result = game
        opponent = opponent_mapping[opponent]
        player = None
        result_score = 0
        if target_result == "X":  # lose
            player = defeats[opponent]
        elif target_result == "Y":  # draw
            player = opponent
            result_score = 3
        elif target_result == "Z":  # win
            player = defeated_by[opponent]
            result_score = 6
        tourname_score += result_score + scores[player]
    return tourname_score


if __name__ == "__main__":
    input_files = [
        input_parsers.INPUTS_DIR / file for file in ["02_test_input", "02_input"]
    ]
    for file in input_files:
        print(f"\t{file.name:=^20}")
        print(f"\t{solve_part_one(file)}")
        print(f"\t{solve_part_two(file)}")
