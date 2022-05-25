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
    all_sequences = []
    lines = puzzle_input.split('\n')
    print(lines, '\n\n')
    for line in lines:
        spl = line.split(' | ')
        four_sequence = spl[1].strip().split()
        all_sequences.append(four_sequence)

    return all_sequences


def find_unique_segments(line):
    found = 0
    for index, entry in enumerate(line):
        if len(entry) == 4:
            print(f'Number 4 is represented by sequence {entry} at index {index}')
            found += 1
        elif len(entry) == 2:
            print(f'Number 1 is represented by sequence {entry} at index {index}')
            found += 1
        elif len(entry) == 3:
            print(f'Number 7 is represented by sequence {entry} at index {index}')
            found += 1
        elif len(entry) == 7:
            print(f'Number 8 is represented by sequence {entry} at index {index}')
            found += 1

    return found


def parse_lines(all_sequences):
    """Given a list of two-tuples, parse them for unique entries."""
    total = 0
    for index, seq in enumerate(all_sequences):
        print(f'Starting at line {index + 1}\n')
        # ten_sequence = seq[0]
        # four_sequence = seq[1]
        # find_unique_segments(ten_sequence)
        found = find_unique_segments(seq)
        if found:
            total += found
        print('\n\n')

    return total


def main():
    # puzzle_input = get_puzzle_input(sample=True)
    puzzle_input = get_puzzle_input()
    all_sequences = get_initial_state(puzzle_input)
    num_found = parse_lines(all_sequences)
    print(f'\n\nFound a total of {num_found} sequences')


if __name__ == '__main__':
    main()
