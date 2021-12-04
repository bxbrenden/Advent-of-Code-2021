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


def get_oxygen_rating(diagnostics, index=0):
    """Get the oxygen-generator rating given a list of diagnostic binary strings.

       Return the rating as a two-tuple: (decimal, binary).
    """
    # Data wrangling to make diags into a transposed numpy array
    grid = []
    for d in diagnostics:
        ld = list(d)
        grid.append(ld)

    arr = np.array(grid)
    arr = arr.transpose()

    freqs = []
    for row in arr:
        c = Counter(row)
        if c['0'] > c['1']:
            freqs.append('0')
        elif c['1'] > c['0']:
            freqs.append('1')
        elif c['1'] == c['0']:
            freqs.append('1')

    # Decide which original diagnostics values to keep
    keepers = []
    for d in diagnostics:
        if d[index] == freqs[index]:
            keepers.append(d)

    print(f'After iteration {index + 1}, the following values were kept for oxygen:')
    for k in sorted(keepers):
        print(k)
    print()

    if len(keepers) == 1:
        return keepers[0]
    else:
        index += 1
        return get_oxygen_rating(keepers, index)


def get_co2_rating(diagnostics, index=0):
    """Get  the CO2 scrubber rating from the diagnostics."""
    # Data wrangling to make diags into a transposed numpy array
    grid = []
    for d in diagnostics:
        ld = list(d)
        grid.append(ld)

    arr = np.array(grid)
    arr = arr.transpose()

    freqs = []
    for row in arr:
        c = Counter(row)
        if c['0'] > c['1']:
            freqs.append('1')
        elif c['1'] > c['0']:
            freqs.append('0')
        elif c['1'] == c['0']:
            freqs.append('0')
    print(f'The value of freqs is: {freqs}')

    # Decide which original diagnostics values to keep
    keepers = []
    for d in diagnostics:
        if d[index] == freqs[index]:
            keepers.append(d)

    print(f'After iteration {index + 1}, the following values were kept for co2:')
    for k in sorted(keepers):
        print(k)
    print()

    if len(keepers) == 1:
        return keepers[0]
    else:
        index += 1
        return get_co2_rating(keepers, index)


def get_life_support_rating(oxygen, co2):
    """Calculate life-support rating."""
    o = int(oxygen, 2)
    c = int(co2, 2)
    return o * c


def main():
    USAGE = 'py3 day03_part1.py <INPUT_FILE>'
    try:
        puzzle_input = read_input_file(sys.argv[1])
    except IndexError:
        raise SystemExit(USAGE)

    oxy = get_oxygen_rating(puzzle_input)
    print(f'The oxygen generator rating is: {oxy}')
    co2 = get_co2_rating(puzzle_input)
    print(f'The CO2 rating is: {co2}')
    life_support = get_life_support_rating(oxy, co2)
    print(f'The life support rating is: {life_support}')


if __name__ == '__main__':
    main()
