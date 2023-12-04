
def parse_file(filename):

    # read file, strip and split according to new line character
    file_data = open(filename, 'r').read().strip().split('\n')
    num_of_lines = len(file_data)
    num_of_chars = len(file_data[0])

    engine = 0

    for row_number, row_item in enumerate(file_data):
        for column_number, column_item in enumerate(row_item):
            if column_item != "*":
                continue

            collision_set = set()

            for current_row in [row_number-1, row_number, row_number+1]:
                for current_column in [column_number-1, column_number, column_number+1]:
                    if current_row < 0 or current_row >= num_of_lines or current_column < 0 or current_column >= num_of_chars or not file_data[current_row][current_column].isdigit():
                        continue
                    while current_column > 0 and file_data[current_row][current_column-1].isdigit():
                        current_column -= 1
                    collision_set.add((current_row, current_column))

            if len(collision_set) != 2:
                continue

            engine_sum = []
            for row, column in collision_set:
                number = ""
                while column < num_of_chars and file_data[row][column].isdigit():
                    number += file_data[row][column]
                    column += 1
                engine_sum.append(int(number))

            engine += engine_sum[0] * engine_sum[1]

    print(f"Engine number is: {engine}")


if __name__ == "__main__":
    parse_file(filename="day3/puzzle.txt")
