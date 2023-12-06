
# print({fields[0]:   fields[1].split()
#        for line in open("day6/example.txt", 'r')
#        if True and (fields := line.strip().split(':'))})


def execute_code(filename='day6/example.txt'):

    data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split(':')
            data.append(line[1].replace(' ', ''))

    winning_counts = 1
    boundary = calculate_boundary(data[0], data[1])
    winning_possibilities = boundary[1] - boundary[0] + 1
    winning_counts *= winning_possibilities

    print(f"{winning_counts=}")


def calculate_boundary(parameter, condition):
    boundary = get_boundary(int(parameter))
    outcome = calculate_outcome(boundary[0], boundary[1])
    while outcome > int(condition):
        boundary[0] -= 1
        boundary[1] += 1
        outcome = calculate_outcome(boundary[0], boundary[1])
    return (boundary[0], boundary[1])


def get_boundary(integer_value):
    lower_bound = 0
    upper_bound = 0
    if integer_value % 2 == 0:
        lower_bound = int(integer_value/2)
        upper_bound = lower_bound
    else:
        lower_bound = int(integer_value/2)
        upper_bound = int(integer_value/2) + 1
    if lower_bound != 0 and upper_bound != 0:
        return [lower_bound, upper_bound]


def calculate_outcome(value1, value2):
    return value1 * value2


if __name__ == "__main__":
    execute_code(filename='day6/puzzle.txt')
