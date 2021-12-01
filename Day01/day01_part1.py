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


def find_all_depth_increases(depths):
    """Given a list of depths, return the number of depths that are
       larger than their predecessors."""
    increases = 0
    annotations = []
    for index, depth in enumerate(depths):
        anno = f'Index: {index}, depth: {depth}'
        if index == 0:
            anno += ' (N/A - no previous measurement)'
            anno += f' increases: {increases}'
            annotations.append(anno)
        else:
            if depth > depths[index - 1]:
                increases += 1
                anno += ' (increased)'
            elif depth <= depths[index - 1]:
                anno += ' (didn\'t increase)'
            anno += f' increases: {increases}'
            annotations.append(anno)

    for anno in annotations:
        print(anno)
    return increases


def main():
    USAGE = 'py3 day01_part1.py <INPUT_FILE>'
    try:
        INPUT_FILE = sys.argv[1]
    except IndexError:
        raise SystemExit(USAGE)
    depths = read_input_file(INPUT_FILE)
    increases = find_all_depth_increases(depths)
    print(f'The number of increases is {increases}')


if __name__ == '__main__':
    main()
