import re


def get_symbol_locations(line):
    symbol_locations = line.replace(".", "0")
    symbol_locations = symbol_locations.replace("\n", "")
    symbol_locations = re.findall(r"\D+", symbol_locations)
    symbol_location_list = []
    for symbol_location in symbol_locations:
        symbol_location_list.append(line.find(symbol_location))
    return symbol_location_list


def get_number_locations(line):
    number_location_list = []
    number_locations = re.findall(r"\d+", line)
    for number_location in number_locations:
        number_location_list.append(
            line.find(number_location), number_location.len())
    return number_location_list


def compare_numberline_with_symbol_line(line, symbol_locations):
    line_number_locations = get_number_locations(line)
    line_number_locations_collisions = []
    for line_number_location in line_number_locations:
        start_position_of_current_number = line.find(line_number_location)
        end_position_of_current_number = (
            start_position_of_current_number + len(line_number_location))
        for symbol_location in symbol_locations:
            if ((symbol_location >= (start_position_of_current_number - 1)) and (symbol_location <= (end_position_of_current_number))):
                line_number_locations_collisions.append(line_number_location)
    return line_number_locations_collisions


def parser(filename="day3/example.txt"):

    engine_sum = 0
    with open(filename, "r") as fd:
        lines = fd.readlines()

        previous_line = ""
        prev_line_numbers = []
        prev_line_symbols_locations = []

        for line in lines:
            modified_line = list(line)
            if previous_line == "":
                previous_line = line
                previous_line_symbols_locations = get_symbol_locations(
                    previous_line)
                prev_line_numbers = get_number_locations(line)
                continue

            current_line_numbers = get_number_locations(line)
            current_line_numbers_collided = compare_numberline_with_symbol_line(
                line, prev_line_symbols_locations)

            for collided_line in current_line_numbers_collided:
                engine_sum += int(collided_line)
                line_replace_start = line.find(collided_line)
                line_replace_end = line_replace_start + len(collided_line)
                for i in range(line_replace_start, line_replace_end):
                    modified_line[i] = "."

            current_line_symbols_locations = get_symbol_locations(line)
            prev_line_collided = compare_numberline_with_symbol_line(
                previous_line, current_line_symbols_locations)

            for prev_collided_line in prev_line_collided:
                engine_sum += int(prev_collided_line)

            # current line collision with current line symbol
            current_line_numbers_collided = compare_numberline_with_symbol_line(
                line, current_line_symbols_locations)

            for collided_line in current_line_numbers_collided:
                engine_sum += int(collided_line)
                line_replace_start = line.find(collided_line)
                line_replace_end = line_replace_start + len(collided_line)
                for i in range(line_replace_start, line_replace_end):
                    modified_line[i] = "."

            previous_line = "".join(modified_line)
            prev_line_numbers = get_number_locations(previous_line)
            prev_line_symbols_locations = get_symbol_locations(previous_line)
        print(f"Engine sum: {engine_sum}")


if __name__ == "__main__":
    parser("day3/puzzle.txt")
    # parser("day3/example.txt")
