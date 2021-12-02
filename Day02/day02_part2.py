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


def calc_depth_and_horiz(directions):
    """Given a list of directions, calculate the aim, depth and horiz. position."""
    aim = 0
    depth = 0
    horiz = 0
    for d in directions:
        magnitude = int(d.split()[1])
        if d.startswith('forward'):
            horiz += magnitude
            depth += magnitude * aim
        elif d.startswith('up'):
            aim -= magnitude
        elif d.startswith('down'):
            aim += magnitude

    return (depth, horiz)


def main():
    USAGE = 'py3 day02_part1.py <INPUT_FILE>'
    try:
        puzzle_input = read_input_file(sys.argv[1])
    except IndexError:
        raise SystemExit(USAGE)

    depth, horiz = calc_depth_and_horiz(puzzle_input)
    print(f'The depth is {depth}, and the horizontal position is {horiz}.')

    product = depth * horiz
    print(f'The product of depth and horizontal position is {product}.')


if __name__ == '__main__':
    main()
