def get_puzzle_input(sample=False):
    """Get the input for the puzzle and return as a string."""
    if sample:
        puzzle_input = 'sample_input.txt'
    else:
        puzzle_input = 'input.txt'
    try:
        with open(puzzle_input, 'r') as si:
            sample_input = si.read().strip()
            return sample_input
    except FileNotFoundError:
        raise SystemExit(f'Could not open {puzzle_input}. No such file.')
    except PermissionError:
        raise SystemExit(f'Could not open {puzzle_input}. Permission denied.')


def get_initial_state(puzzle_input):
    """Parse the data using the specified format."""
    spl = puzzle_input.split('|')
    ten_sequence = spl[0].strip().split()
    four_sequence = spl[1].strip().split()

    return (ten_sequence, four_sequence)


def find_unique_segments(line):
    for index, entry in enumerate(line):
        if len(entry) == 4:
            print(f'Number 4 is represented by sequence {entry} at index {index}')
        elif len(entry) == 2:
            print(f'Number 1 is represented by sequence {entry} at index {index}')
        elif len(entry) == 3:
            print(f'Number 7 is represented by sequence {entry} at index {index}')
        elif len(entry) == 7:
            print(f'Number 8 is represented by sequence {entry} at index {index}')


def main():
    puzzle_input = get_puzzle_input(sample=True)
    # puzzle_input = get_puzzle_input()
    ten_sequence, four_sequence = get_initial_state(puzzle_input)
    print(ten_sequence, four_sequence)
    find_unique_segments(ten_sequence)
    find_unique_segments(four_sequence)


if __name__ == '__main__':
    main()
