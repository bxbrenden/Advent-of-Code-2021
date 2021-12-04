from collections import Counter
import sys
import numpy as np


def read_input_file(filename):
    """Read the input file for the challenge."""
    try:
        with open(filename, 'r') as inp:
            input_file = inp.read().strip()
            input_lines = input_file.split('\n')
            return input_lines
    except FileNotFoundError:
        print(f'Input file {filename} not found.')
        raise SystemExit
    except PermissionError:
        print(f'Input file {filename} exists, but permission denied.')
        raise SystemExit


def get_oxygen_rating(diagnostics):
    """Get the oxygen-generator rating given a list of diagnostic binary strings.

       Return the rating as a two-tuple: (decimal, binary).
    """
    pass


def get_co2_rating(diagnostics):
    """Get  the CO2 scrubber rating from the diagnostics."""
    pass


def get_life_support_rating(oxygen, co2):
    """Calculate life-support rating."""
    return oxygen * co2


def main():
    USAGE = 'py3 day03_part1.py <INPUT_FILE>'
    try:
        puzzle_input = read_input_file(sys.argv[1])
    except IndexError:
        raise SystemExit(USAGE)


if __name__ == '__main__':
    main()
