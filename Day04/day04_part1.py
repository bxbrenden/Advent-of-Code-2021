import sys

import numpy as np
import pandas as pd


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
    boards = [np.array([[int(x) for x in b.split(' ') if x != '']
              for b in board.split('\n') if b != ''])
              for board in boards_strs]

    return (numbers, boards)


class BingoBoard:
    def __init__(self, array):
        self.board = array
        self.grid = np.zeros((5, 5))
        self.bingo = False
        self.bingo_index = list('BINGO')

    def __str__(self):
        board_df = pd.DataFrame(self.board,
                                index=self.bingo_index,
                                columns=self.bingo_index,
                                dtype=np.int8)
        grid_df = pd.DataFrame(self.grid,
                               index=self.bingo_index,
                               columns=self.bingo_index,
                               dtype=np.int8)
        return str(pd.concat([board_df, grid_df], axis=1))

    def update(self, number):
        """Given a number, update the grid in the bingo board from 0 to 1."""
        if hit := np.where(self.board == number):
            hit_x = hit[0][0]
            hit_y = hit[1][0]
            self.grid[hit_x][hit_y] = 1

    def check_for_bingo(self):
        row_sums = []
        col_sums = []
        for n in range(len(self.grid)):
            row_sums.append(np.sum(self.grid[n]))

        cols = self.grid.transpose()
        for m in range(len(cols)):
            col_sums.append(np.sum(cols[m]))

        if 5 in row_sums or 5 in col_sums:
            print('BINGO WAS HIS NAME-OH!\n')
            print(self)
            return True


def main():
    USAGE = 'py3 day04_part1.py <INPUT_FILE>'
    try:
        inp = read_input_file(sys.argv[1])
    except IndexError:
        raise SystemExit(USAGE)

    numbers, boards = get_numbers_and_boards(inp)

    bingo_boards = []
    for board in boards:
        b = BingoBoard(board)
        bingo_boards.append(b)

    bingo = False
    for num in numbers:
        for b in bingo_boards:
            b.update(num)
            print(b, '\n\n')
            if b.check_for_bingo():
                bingo = True
        if bingo is True:
            break


if __name__ == '__main__':
    main()
