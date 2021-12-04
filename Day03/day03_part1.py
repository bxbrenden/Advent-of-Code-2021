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


def get_gamma_rate(diagnostics):
    """Get the gamma rate given a list of diagnostic binary strings.i

       Return the gamma rate as a two-tuple: (decimal, binary).
    """
    # Make a list of lists where each entry is a single character: '0' or '1'
    grid = []
    for d in diagnostics:
        ld = list(d)
        grid.append(ld)

    # Convert list of lists to numpy array
    arr = np.array(grid)

    # Swap rows and columns to get counts
    arr = arr.transpose()

    # Get the frequencies of 1s and 0s for each column (now row)
    gamma = []
    for index, _ in enumerate(arr):
        c = Counter(arr[index])
        if c['0'] > c['1']:
            gamma.append('0')
        else:
            gamma.append('1')

    # Clean up gamma to be a single string
    gamma_bin_str = ''.join(gamma)

    # Convert to decimal
    gamma_dec = int(gamma_bin_str, 2)

    return (gamma_bin_str, gamma_dec)


def get_epsilon_from_gamma(gamma):
    """Use the gamma binary-string value to get the epsilon."""
    # '01000'.translate(str.maketrans('01', '10'))
    return int(gamma.translate(str.maketrans('01', '10')), 2)


def get_power_consumption(gamma, epsilon):
    """Calculate power consumption."""
    return gamma * epsilon


def main():
    USAGE = 'py3 day03_part1.py <INPUT_FILE>'
    try:
        puzzle_input = read_input_file(sys.argv[1])
    except IndexError:
        raise SystemExit(USAGE)

    gamma_bin, gamma_decimal = get_gamma_rate(puzzle_input)
    print(f'The gamma rate is: {gamma_decimal}')
    epsilon = get_epsilon_from_gamma(gamma_bin)
    print(f'The epsilon rate is {epsilon}')
    power = get_power_consumption(gamma_decimal, epsilon)
    print(f'The power consumption is {power}')


if __name__ == '__main__':
    main()
