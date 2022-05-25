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
    """Split by commas and return as a list of ints."""
    return puzzle_input.split(',')


def print_status(state, num_days, first_run=False):
    """Print the status of the puzzle input's current value."""
    fish = ','.join(state)
    if first_run:
        template = f'Initial State: {fish}'
    elif num_days == 1:
        template = f'After {num_days} day: {fish}'
    else:
        template = f'After {num_days} days: {fish}'
    print(template)


def main():
    puzzle_input = get_puzzle_input(sample=True)
    initial_state = get_initial_state(puzzle_input)
    print_status(initial_state, 0, first_run=True)
    print_status(initial_state, 1)
    print_status(initial_state, 2)


if __name__ == '__main__':
    main()
