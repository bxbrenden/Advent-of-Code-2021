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


def get_all_triplet_increases(depths):
    """Given a list of depths, return the answer to Day01, Part2."""
    increases = 0
    annotations = []

    for index, depth in enumerate(depths):
        anno = []
        anno.append(index)
        if index == 0 or index == 1:
            continue
        if index == 2:
            triplet = int(depth) + int(depths[index - 1]) + int(depths[index - 2])
            anno.append(triplet)
            anno.append('(N/A)')
            anno.append('False')
            anno.append(increases)
        if index >= 3:
            try:
                new_triplet = int(depth) + int(depths[index - 1]) + int(depths[index - 2])
                old_triplet = int(depths[index - 1]) + int(depths[index - 2]) + int(depths[index - 3])
                anno.append(new_triplet)
                anno.append(old_triplet)
                if new_triplet > old_triplet:
                    anno.append('True')
                    increases += 1
                else:
                    anno.append('False')
                anno.append(increases)
            except IndexError:
                print(f'Index Error encountered at index {index} with depth {depth}')
        annotations.append(anno)

    columns = ['Index', 'Current', 'Previous', 'Increased', 'Total Increases']
    table_header = f'{columns[0]:<12}{columns[1]:<17}{columns[2]:<17}{columns[3]:<15}{columns[4]:<20}'
    print(table_header)
    for anno in annotations:
        output = f'{anno[0]:<12}{anno[1]:<17}{anno[2]:<17}{anno[3]:<15}{anno[4]:<20}'
        print(output)
    return increases


def main():
    USAGE = 'py3 day01_part1.py <INPUT_FILE>'
    try:
        INPUT_FILE = sys.argv[1]
    except IndexError:
        raise SystemExit(USAGE)
    depths = read_input_file(INPUT_FILE)
    increases = get_all_triplet_increases(depths)

    print(f'The number of increases is {increases}')


if __name__ == '__main__':
    main()
