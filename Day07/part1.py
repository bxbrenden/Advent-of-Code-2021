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
    """Split by commas and make everything an int."""
    return([int(x) for x in puzzle_input.split(',')])


def main():
    puzzle_input = get_puzzle_input(sample=True)
    initial_state = get_initial_state(puzzle_input)
    print(initial_state)


if __name__ == '__main__':
    main()
