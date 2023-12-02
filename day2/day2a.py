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
    data = []
    game_substring = "Game "
    sum = 0
    with open(filename, "r") as fd:
        lines = fd.readlines()
        for line in lines:
            line_id = line.split(':')
            line_id[0] = line_id[0].replace(game_substring, "")

            list_outcomes = []
            game_outcomes = line_id[1].split(';')
            red = 0
            green = 0
            blue = 0
            should_not_add = False
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

                    if (red > 12 or green > 13 or blue > 14):
                        should_add = False
                        break
                    else:
                        should_add = True
                if (not should_add):
                    should_not_add = True
                    break
                should_not_add = False
                list_outcomes.append((red, green, blue))
            if (should_not_add):
                continue
            data.append((int(line_id[0]), list_outcomes))
            sum += int(line_id[0])

        print(data)
        print(sum)


if __name__ == "__main__":
    parse_game_id(filename="day2/puzzle.txt")
