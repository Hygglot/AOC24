# Advent of code Year 2024 Day 1 solution
# Author = Hugo Ekinge
# Date = December 2024

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

# Convert each line of input into a list of integers
numbers = [list(map(int, line.split())) for line in input]

# Zip the list of pairs into two separate lists, col1 and col2
col1, col2 = zip(*numbers)

# Sort the first column
sorted_col1 = sorted(col1)

# Sort the second column
sorted_col2 = sorted(col2)



result1 = sum(abs(a - b) for a, b in zip(sorted_col1, sorted_col2))

result2 = sum(a * col2.count(a) for a in col1)

print("Part One : "+ str(result1))
print("Part Two : "+ str(result2))