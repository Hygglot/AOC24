import re

# Advent of code Year 2024 Day 3 solution
# Author = Hugo Ekinge
# Date = December 2024

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

tot = 0
l = input.strip()
matches = re.findall(r'mul\((\d+),(\d+)\)', l)
for match in matches:
    print(match)
    x, y = map(int, match)
    tot += x * y

tot2 = 0
e = True
for s in re.split(r'do\(\)', l):
    s = re.split(r'don\'t\(\)', s)[0]
    print(s)
    if e:
        matches = re.findall(r'mul\((\d+),(\d+)\)', s)
        for match in matches:
            print(match)
            x, y = map(int, match)
            tot2 += x * y

print("Part One : "+ str(tot))

print("Part Two : "+ str(tot2))