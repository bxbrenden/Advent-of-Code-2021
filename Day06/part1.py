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
    return [int(x) for x in puzzle_input.split(',')]


def print_status(state, num_days, first_run=False):
    """Print the status of the puzzle input's current value."""
    fish = ','.join([str(x) for x in state])
    if first_run:
        template = f'Initial state: {fish}'
    elif num_days == 1:
        template = f'After  {num_days} day:  {fish}'
    elif num_days > 1 and num_days < 10:
        template = f'After  {num_days} days: {fish}'
    else:
        template = f'After {num_days} days: {fish}'
    print(template)


def circle_of_life(state):
    """Propagate the lanternfish species."""
    new_state = []
    new_fish = []
    for s in state:
        if s > 0:
            s -= 1
            new_state.append(s)
        elif s == 0:
            s = 6
            new_state.append(s)
            new_fish.append(8)

    final_state = new_state + new_fish

    return final_state


def calculate_lanternfish(state, day, num_days, first_run=False):
    """Calculate the number of lanternfish and display the results."""
    if first_run:
        print_status(state, day, first_run=True)
        fish = state
    else:
        fish = circle_of_life(state)
        print_status(fish, day)

    day += 1
    if day < num_days:
        return calculate_lanternfish(fish, day, num_days)
    else:
        return fish


def get_lanternfish_population(fish):
    return len(fish)


def main():
    # puzzle_input = get_puzzle_input(sample=True)
    puzzle_input = get_puzzle_input()
    NUM_DAYS = 81
    initial_state = get_initial_state(puzzle_input)
    lanternfish = calculate_lanternfish(initial_state, 0, NUM_DAYS, first_run=True)
    # print(lanternfish)
    population = get_lanternfish_population(lanternfish)
    print(f'\nThere are {population} lanternfish.')


if __name__ == '__main__':
    main()
