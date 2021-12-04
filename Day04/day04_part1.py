import sys

import numpy as np


def read_input_file(filename):
    """Read the input file for the challenge."""
    try:
        with open(filename, 'r') as inp:
            input_file = inp.read()
            return input_file
    except FileNotFoundError:
        print(f'Input file {filename} not found.')
        raise SystemExit
    except PermissionError:
        print(f'Input file {filename} exists, but permission denied.')
        raise SystemExit


def get_numbers_and_boards(puzzle_input):
    """Given the puzzle input, return a two-tuple with numbers and boards."""
    splits = puzzle_input.split('\n\n')
    numbers_str = splits[0]
    boards_strs = splits[1:]

    numbers = [int(x) for x in numbers_str.split(',') if x != '']
    boards = [[[int(x) for x in b.split(' ') if x != ''] for b in board.split('\n') if b != ''] for board in boards_strs]

    return (numbers, boards)


def main():
    USAGE = 'py3 day04_part1.py <INPUT_FILE>'
    try:
        inp = read_input_file(sys.argv[1])
    except IndexError:
        raise SystemExit(USAGE)

    for line in inp:
        print(line)

    numbers, boards = get_numbers_and_boards(inp)
    for board in boards:
        print(board)


if __name__ == '__main__':
    main()
