# Advent Code 2021
# link: https://adventofcode.com/
# DAY 2 Problem

read_file = open("input.txt", "r")
output = []
for line in read_file:
    output.append(tuple(line.strip("\n").split()))
print(output)

# Part 1
sub_x = 0
sub_y = 0
for x in output:
    if x[0] == "forward":  # move the sub forward
        sub_x += int(x[1])
    elif x[0] == "down":  # go towards the sea floor
        sub_y += int(x[1])
    elif x[0] == "up":  # go towards the surface
        sub_y -= int(x[1])
print("Part 1:\n\tThe Sub is at: " + str(sub_y * sub_x))

# Part 2
sub_x1 = 0
sub_y1 = 0
aim = 0
for x in output:
    if x[0] == "forward":  # move the sub
        sub_x1 += int(x[1])
        sub_y1 += aim * int(x[1])
    elif x[0] == "down":  # re-adjust aim to the sea floor
        aim += int(x[1])
    elif x[0] == "up":  # re-adjust aim to the surface
        aim -= int(x[1])
print("Part 2:\n\tThe Sub is at: " + str(sub_y1 * sub_x1))
