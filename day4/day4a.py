def parse_file(filename):

    data_file = open(filename, 'r').read().strip().split('\n')
    num_of_lines = len(data_file)
    num_of_chars = len(data_file[0])

    data_in = []
    for line in data_file:
        temp = line.split(":")
        data_in.append(temp[1].split("|"))
    total_points = 0

    for line in data_in:
        matches = 0
        winning_numbers = (line[0].strip().split())
        card_numbers = (line[1].strip().split())
        for winning_item in winning_numbers:
            for card_item in card_numbers:
                if winning_item == card_item:
                    if matches == 0:
                        matches += 1
                    else:
                        matches *= 2
        total_points += matches

    print(f"Total points: {total_points}")


if __name__ == "__main__":
    parse_file(filename="day4/puzzle.txt")
