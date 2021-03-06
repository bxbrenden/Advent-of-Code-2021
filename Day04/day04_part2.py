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
        self.last_called = None
        self.final_score = None
        self.total_called = 0

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
            if hit[0].size > 0:
                hit_x = hit[0][0]
                hit_y = hit[1][0]
                self.grid[hit_x][hit_y] = 1
                self.last_called = number
                self.total_called += 1

    def check_for_bingo(self):
        row_sums = []
        col_sums = []
        for n in range(len(self.grid)):
            row_sums.append(np.sum(self.grid[n]))

        cols = self.grid.transpose()
        for m in range(len(cols)):
            col_sums.append(np.sum(cols[m]))

        if 5 in row_sums or 5 in col_sums:
            print('BINGO WAS HIS NAME-OH!')
            print(f'The last number called was {self.last_called}.\n')
            print(self)
            self.final_score = self.calculate_final_score()
            self.bingo = True
            return True

    def calculate_final_score(self):
        arr_coords = np.where(self.grid == 0)
        x_coords = arr_coords[0].tolist()
        y_coords = arr_coords[1].tolist()
        coords = [z for z in zip(x_coords, y_coords)]
        unmarked = 0
        for c in coords:
            unmarked += self.board[c[0]][c[1]]

        print(f'Sum of the unmarked values on the board: {unmarked}')
        final_score = self.last_called * unmarked
        print(f'FINAL SCORE: {final_score}')
        print(f'Numbers called before hitting Bingo: {self.total_called}')
        return final_score


def calc_all_bingos(numbers, bingo_boards):
    for numindex, num in enumerate(numbers):
        for i, b in enumerate(bingo_boards):
            b.update(num)
            b.check_for_bingo()
            if b.bingo:
                bingo_boards.pop(i)
        if len(bingo_boards == 1):
            return bingo_boards[0]
        else:
            return calc_all_bingos(numbers[numindex:], bingo_boards)


def main():
    USAGE = 'py3 day04_part2.py <INPUT_FILE>'
    try:
        inp = read_input_file(sys.argv[1])
    except IndexError:
        raise SystemExit(USAGE)

    numbers, boards = get_numbers_and_boards(inp)

    bingo_boards = []
    for board in boards:
        b = BingoBoard(board)
        bingo_boards.append(b)

    for num in numbers:
        for b in bingo_boards:
            b.update(num)
            if not b.bingo:
                b.check_for_bingo()
        if all([b.bingo for b in bingo_boards]):
            print('BINGO FOR ALL!!!')
            break


if __name__ == '__main__':
    main()
