
def check_string_number(value):
    """Check if a string is a number, and return the number if it is."""
    if value.find("one") != -1:
        return 1
    elif value.find("two") != -1:
        return 2
    elif value.find("three") != -1:
        return 3
    elif value.find("four") != -1:
        return 4
    elif value.find("five") != -1:
        return 5
    elif value.find("six") != -1:
        return 6
    elif value.find("seven") != -1:
        return 7
    elif value.find("eight") != -1:
        return 8
    elif value.find("nine") != -1:
        return 9
    else:
        return None


def check_number(data):
    if data.isdigit():
        return int(data)
    else:
        return None


def checker():
    data = open("day1/day1.txt", "r")
    # data = open("day1/example2.txt", "r")

    sum = 0

    for line in data:
        first = 0
        firststr = ""
        last = 0
        laststr = ""

        for i in range(len(line)):
            if check_number(line[i]) is not None:
                first = check_number(line[i])
                break
            else:
                firststr += line[i]
                first = check_string_number(firststr)
                if first != None:
                    break
                else:
                    first = 0

        for i in range(len(line)-1, -1, -1):
            if check_number(line[i]) is not None:
                last = check_number(line[i])
                break
            else:
                laststr = line[i] + laststr
                last = check_string_number(laststr)
                if last != None:
                    break
                else:
                    last = 0

        number = (first * 10) + last
        print(f"{line}: {number}")
        sum += number

    print(f"Sum: {sum}")


if __name__ == "__main__":
    checker()
