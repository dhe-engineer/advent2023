# read text file
data = open("day1.txt", "r")
# data = open("example.txt", "r")

# print(f"length of data: {len(data)}")
sum = 0
# iterate through each line in file
for line in data:
    first = 0
    firststr = ""
    last = 0
    laststr = ""
    # look through all characters to find the first and last number in the string
    for i in range(len(line)):
        if line[i].isdigit():
            first = int(line[i])
            break
        else:
            firststr += line[i]

    # look through all characters to find the last number in the string
    for i in range(len(line)-1, -1, -1):
        temp = line[i]
        if line[i].isdigit():
            last = int(line[i])
            break
        else:
            laststr = line[i] + laststr

    number = (first * 10) + last
    # print(f"{line}: {number}")
    sum = sum + number

print(f"Sum: {sum}")
