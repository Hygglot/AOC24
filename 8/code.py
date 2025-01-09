# Advent of code Year 2024 Day 8 solution
# Author = Hugo Ekinge
# Date = December 2023

from itertools import combinations

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

grid = [[ch for ch in line.strip()] for line in input]
freqs = {}
anodes = set()

def in_grid(pos, h, w):
    return not pos[0] < 0 and pos[0] < h and not pos[1] < 0 and pos[1] < w

def antinodes(pos1, pos2):
    diff = (pos1[0]-pos2[0], pos1[1]-pos2[1])
    n1 = (pos1[0]+diff[0], pos1[1]+diff[1])
    n2 = (pos2[0]-diff[0], pos2[1]-diff[1])
    return [p for p in [n1, n2] if in_grid(p, len(grid), len(grid[0]))]

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print(len(grid), len(grid[0]))

print_grid(grid)

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != '.':
            f = grid[row][col]
            pos = (row, col)
            if f not in freqs:
                freqs[f] = [pos]
            else:
                freqs[f].append(pos)

print(freqs)
for f in freqs:
    if len(freqs[f]) > 1:
        for comb in combinations(freqs[f], 2):
            anodes.update(antinodes(comb[0], comb[1]))

def antinodes2(pos1, pos2):
    diff = (pos1[0]-pos2[0], pos1[1]-pos2[1])
    nodes = [pos1, pos2]
    while in_grid((pos1[0]+diff[0], pos1[1]+diff[1]), len(grid), len(grid[0])):
        pos1 = (pos1[0]+diff[0], pos1[1]+diff[1])
        nodes.append(pos1)
    while in_grid((pos2[0]-diff[0], pos2[1]-diff[1]), len(grid), len(grid[0])):
        pos2 = (pos2[0]-diff[0], pos2[1]-diff[1])
        nodes.append(pos2)
    return nodes

anodes2 = set()
for f in freqs:
    if len(freqs[f]) > 1:
        for comb in combinations(freqs[f], 2):
            anodes2.update(antinodes2(comb[0], comb[1]))

print("Part One : "+ str(len(anodes)))



print("Part Two : "+ str(len(anodes2)))