# Advent of code Year 2024 Day 10 solution
# Author = Hugo Ekinge
# Date = December 2023

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

grid = [[int(c) for c in line.strip()] for line in input]

def in_grid(pos, grid):
    h, w = len(grid), len(grid[0])
    return not pos[0] < 0 and pos[0] < h and not pos[1] < 0 and pos[1] < w

def print_grid(grid):    
    for row in grid:
        print("".join(str(c) for c in row))
    print(len(grid), len(grid[0]))

def move(pos, dir):
    return (pos[0]+dir[0], pos[1]+dir[1])

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

def count_trailheads(pos, grid):
    tot = 0
    visited_nines = set()
    to_visit = [(pos, -1)]
    while to_visit:
        pos, val = to_visit.pop()
        curr = grid[pos[0]][pos[1]]
        if curr != val + 1:
            continue
        if curr == 9:
            visited_nines.add(pos)
            tot += 1
            continue
        for dir in DIRS:
            new_pos = move(pos, dir)
            if in_grid(new_pos, grid):
                to_visit.append((new_pos, curr))
    return len(visited_nines), tot

print_grid(grid)

score = 0
rating = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 0:
            ths, thr = count_trailheads((y, x), grid)
            score += ths
            rating += thr

print("Part One : "+ str(score))



print("Part Two : "+ str(rating))