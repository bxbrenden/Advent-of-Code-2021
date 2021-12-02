import sys


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


def main():
    USAGE = 'py3 day02_part1.py <INPUT_FILE>'
    try:
        puzzle_input = read_input_file(sys.argv[1])
    except IndexError:
        raise SystemExit(USAGE)

    for line in puzzle_input:
        print(line)


if __name__ == '__main__':
    main()
