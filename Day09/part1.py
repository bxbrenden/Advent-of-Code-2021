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
    grid = []
    lines = puzzle_input.split('\n')
    for line in lines:
        grid_line = [int(x) for x in list(line)]
        grid.append(grid_line)

    return grid


def find_corners(grid):
    """Given an NxM grid, return a list of the corner coordinates."""
    # top-left will always be a corner and will always be 0, 0
    corners = [(0, 0)]
    top_right = (0, len(grid[0]) - 1)
    bottom_left = (len(grid) - 1, 0)
    bottom_right = (len(grid) - 1, len(grid[0]) - 1)

    for corner in (top_right, bottom_left, bottom_right):
        corners.append(corner)

    return corners


def find_low_point():
    """Find the low points."""
    pass


def main():
    puzzle_input = get_puzzle_input(sample=True)
    # puzzle_input = get_puzzle_input()
    grid = get_initial_state(puzzle_input)
    for row in grid:
        print(row)
    corners = find_corners(grid)
    for corner in corners:
        print(corner)


if __name__ == '__main__':
    main()
