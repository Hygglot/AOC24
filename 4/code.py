# Advent of code Year 2024 Day 4 solution
# Author = Hugo Ekinge
# Date = December 2023

import numpy as np

def in_grid(pos, h, w):
    return not pos[0] < 0 and pos[0] < h and not pos[1] < 0 and pos[1] < w

def new_pos(pos, dir):
    if dir == 0:
        return (pos[0], pos[1]+1)
    elif dir == 1:
        return (pos[0]-1, pos[1])
    elif dir == 2:
        return (pos[0], pos[1]-1)
    elif dir == 3:
        return (pos[0]+1, pos[1])

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

grid = np.array([[ch for ch in row] for row in input.split()])

grid = [line.rstrip() for line in input.split()]
directions = [(-1,0), (0,1), (1,0), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]

tot = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'X':
            for dir in directions:
                pos = (row, col)
                valid = True
                for c in "MAS":
                    pos = (pos[0]+dir[0], pos[1]+dir[1])
                    if in_grid(pos, len(grid), len(grid[0])) and grid[pos[0]][pos[1]] == c:
                        continue
                    else:
                        valid = False
                        break
                if valid:
                    tot += 1

directions = [(1,1), (-1,-1), (-1,1), (1,-1)]

tot2 = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'A':
            valid = True
            pos = (row, col)
            corners = []
            for dir in directions:
                if not in_grid((pos[0]+dir[0], pos[1]+dir[1]), len(grid), len(grid[0])):
                    valid = False
                    break
                corners.append(grid[pos[0]+dir[0]][pos[1]+dir[1]])
            if valid and len(corners) == 4:
                if corners[:2].count('S') == 1 and corners[:2].count('M') == 1:
                    if corners[2:].count('S') == 1 and corners[2:].count('M') == 1:
                        tot2 += 1


print("Part One : "+ str(tot))

print("Part Two : "+ str(tot2))