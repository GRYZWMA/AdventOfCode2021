# Advent Code 2021
# link: https://adventofcode.com/
# DAY 1 Problem

with open('input.txt') as input_file:
    read_data = input_file.readlines()
    read_data = [line[:-1] for line in read_data]
    read_data = [int(i) for i in read_data]

count = 0
index = 0

for x in range(len(read_data) - 3):
    lower = read_data[x] + read_data[x + 1] + read_data[x + 2]
    upper = read_data[x + 1] + read_data[x + 2] + read_data[x + 3]
    if lower < upper:
        count += 1
        index += 1
    else:
        index += 1

print("Day 1 Part 1 Answer: " + str(count))

count1 = 0
index1 = 0

for y in range(len(read_data) - 1):
    if read_data[y] < read_data[y + 1]:
        count1 += 1
        index1 += 1
    else:
        index1 += 1

print("Day 1 Part 2 Answer: " + str(count1))
