def replace_line(data, parser):
    if (data.find(parser) != -1):
        data = data.replace(parser, "")
        try:
            return int(data)
        except ValueError:
            # Impossible
            return -1
    else:
        return -1


def parse_game_id(filename="day2/example.txt"):
    game_substring = "Game "
    sum = 0
    with open(filename, "r") as fd:
        lines = fd.readlines()
        for line in lines:
            line_id = line.split(':')
            line_id[0] = line_id[0].replace(game_substring, "")

            list_outcomes = []
            game_outcomes = line_id[1].split(';')
            red_max = 0
            green_max = 0
            blue_max = 0
            red = 0
            green = 0
            blue = 0
            for outcome in game_outcomes:
                # outcome = outcome.strip()
                outcome = outcome.split(',')
                red = 0
                green = 0
                blue = 0
                should_add = False
                for item in outcome:
                    should_add = False
                    red_parse = replace_line(item, " red")
                    green_parse = replace_line(item, " green")
                    blue_parse = replace_line(item, " blue")

                    if (red_parse != -1):
                        red = red_parse
                    if (green_parse != -1):
                        green = green_parse
                    if (blue_parse != -1):
                        blue = blue_parse

                    if (red > red_max):
                        red_max = red
                    if (green > green_max):
                        green_max = green
                    if (blue > blue_max):
                        blue_max = blue
            sum += red_max * green_max * blue_max

        print(sum)


if __name__ == "__main__":
    parse_game_id(filename="day2/puzzle.txt")
