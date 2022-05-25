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


def is_top_row(coord):
    """Return True if coordinate is in the top row."""
    if coord[0] == 0:
        return True
    else:
        return False


def is_bottom_row(coord, grid):
    """Return True if coordinate is in the bottom row."""
    if coord[0] == len(grid) - 1:
        return True
    else:
        return False


def is_left_column(coord):
    """Return True if coordinate is in the leftmost column."""
    if coord[1] == 0:
        return True
    else:
        return False


def is_right_column(coord, grid):
    """Return True if coordinateis in the rightmost column."""
    if coord[1] == len(grid[0]) - 1:
        return True
    else:
        return False


def find_low_points(grid):
    """Find the low points."""
    low_points = []
    risks = []
    for x, row in enumerate(grid):
        for y, column in enumerate(row):
            current = (x, y)
            point = grid[x][y]
            # Check for top-left corner
            if is_top_row(current) and is_left_column(current):
                print(f'Found top-left corner at ({x}, {y})). Value = {grid[x][y]}')
                # If right and below are greater, this is a low point
                right = grid[x][y+1]
                below = grid[x+1][y]
                if right > point and below > point:
                    low_points.append(current)
                    risks.append(point)
            # Check for top-right corner
            elif is_top_row(current) and is_right_column(current, grid):
                print(f'Found top-right corner at ({x}, {y})). Value = {grid[x][y]}')
                # If left and below are greater, this is a low point
                left = grid[x][y-1]
                below = grid[x-1][y]
                if left > point and below > point:
                    low_points.append(current)
                    risks.append(point)
            # Check for top row
            elif is_top_row(current):
                # If left, right, and below are greater, this is a low point
                left = grid[x][y-1]
                right = grid[x][y+1]
                below = grid[x-1][y]
                if left > point and right > point and below > point:
                    low_points.append(current)
                    risks.append(point)
            # Check for bottom-left corner
            elif is_bottom_row(current, grid) and is_left_column(current):
                print(f'Found bottom-left corner at ({x}, {y})). Value = {grid[x][y]}')
                # If right and above are greater, this is a low point
                right = grid[x][y+1]
                above = grid[x-1][y]
                if right > point and above > point:
                    low_points.append(current)
                    risks.append(point)
            # Check for bottom-right corner
            elif is_bottom_row(current, grid) and is_right_column(current, grid):
                print(f'Found bottom-right corner at ({x}, {y})). Value = {grid[x][y]}')
                # If left and above are greater, this is a low point
                left = grid[x][y-1]
                above = grid[x-1][y]
                if left > point and above > point:
                    low_points.append(current)
                    risks.append(point)
            # Check for bottom row
            elif is_bottom_row(current, grid):
                # If left, right, and above are greater, this is a low point
                left = grid[x][y-1]
                right = grid[x][y+1]
                above = grid[x-1][y]
                # if left > point and right > point and above > point:
                if min(left, right, above, point) == point:
                    low_points.append(current)
                    risks.append(point)
            # Check for left column
            elif is_left_column(current):
                # If right, above, and below are greater, this is a low point
                right = grid[x][y+1]
                above = grid[x-1][y]
                below = grid[x+1][y]
                if min(right, above, below, point) == point:
                    low_points.append(current)
                    risks.append(point)
            # Check for right column
            elif is_right_column(current, grid):
                # If left, above, and below are greater, this is a low point
                left = grid[x][y-1]
                above = grid[x-1][y]
                below = grid[x+1][y]
                if min(left, above, below, point) == point:
                    low_points.append(current)
                    risks.append(point)
            # All others have 4 adjacents:
            else:
                # If left, right, above, and below are greater, this is a low point:
                left = grid[x][y-1]
                right = grid[x][y+1]
                above = grid[x-1][y]
                below = grid[x+1][y]
                if min(left, right, above, below, point) == point:
                    low_points.append(current)
                    risks.append(point)
    return (low_points, risks)


def main():
    puzzle_input = get_puzzle_input(sample=True)
    # puzzle_input = get_puzzle_input()
    grid = get_initial_state(puzzle_input)
    for row in grid:
        print(row)
    corners = find_corners(grid)
    for corner in corners:
        print(corner)

    # Testing the coordinates of my two-dimensional array

    # top = (0, 2)
    # left = (1, 0)
    # right = (3, 9)
    # bottom = (4, 5)

    # assert is_top_row(top)
    # assert is_left_column(left)
    # assert is_right_column(right, grid)
    # assert is_bottom_row(bottom, grid)

    # Isolate the corners
    # top_left = corners[0]
    # top_right = corners[1]
    # bottom_left = corners[2]
    # bottom_right = corners[3]

    # assert (is_top_row(top_left) and is_left_column(top_left))
    # assert (is_top_row(top_right) and is_right_column(top_right, grid))
    # assert (is_bottom_row(bottom_left, grid) and is_left_column(bottom_left))
    # assert (is_bottom_row(bottom_right, grid) and is_right_column(bottom_right, grid))

    low_points, risks = find_low_points(grid)
    print(f'Low point coordinates:\n{low_points}')
    for risk in risks:
        print(risk + 1)
    total_risk = sum([x+1 for x in risks])
    print(f'Total risk: {total_risk}')


if __name__ == '__main__':
    main()
