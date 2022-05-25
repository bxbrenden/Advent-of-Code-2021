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


def calculate_cost(puzzle_input):
    """Calculate the cost of moving."""
    # use giant number so total cost is initially very high
    #   this is a hack :-/
    total_cost = 1_000_000_000_000_000
    home_base_index = 0

    for index in range(len(puzzle_input)):
        current_cost = 0
        home_base = puzzle_input[index]
        for p in puzzle_input:
            cost = abs(p - home_base)
            current_cost += cost

        if current_cost < total_cost:
            total_cost = current_cost
            home_base_index = index

    return (home_base_index, total_cost)


def main():
    # puzzle_input = get_puzzle_input(sample=True)
    puzzle_input = get_puzzle_input()
    initial_state = get_initial_state(puzzle_input)
    print(initial_state)
    cheapest_place, cost = calculate_cost(initial_state)
    print(f'Cheapest place to move: {cheapest_place}, cost: {cost}')


if __name__ == '__main__':
    main()
