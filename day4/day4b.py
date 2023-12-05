def parse_file(filename):

    data_file = open(filename, 'r').read().strip().split('\n')
    num_of_lines = len(data_file)
    num_of_chars = len(data_file[0])

    new_scratch_card = []
    for numbers in range(num_of_lines):
        new_scratch_card.append(int(1))

    data_in = []
    for line in data_file:
        temp = line.split(":")
        data_in.append(temp[1].split("|"))
    total_points = 0

    for line_number, line in enumerate(data_in):
        matches = 0
        winning_numbers = (line[0].strip().split())
        card_numbers = (line[1].strip().split())
        number_of_card_copies = new_scratch_card[line_number]

        for winning_item in winning_numbers:
            for card_item in card_numbers:
                if winning_item == card_item:
                    matches += 1

        for winning_range in range(0, number_of_card_copies):
            for increment_number in range(line_number+1, line_number+matches+1):
                if increment_number > num_of_lines:
                    break
                current_number = int(new_scratch_card[increment_number])
                new_scratch_card[increment_number] = current_number + 1

        total_points += matches

    print(f"Total points: {total_points}, Total cards: {
          sum(new_scratch_card)}")


if __name__ == "__main__":
    # parse_file(filename="day4/example.txt")
    parse_file(filename="day4/puzzle.txt")
