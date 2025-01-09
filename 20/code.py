# Advent of code Year 2024 Day 20 solution
# Author = Hugo Ekinge
# Date = December 2024

import heapq

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

grid = [[c for c in line.strip()] for line in input]
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            start_pos = (y, x)
        elif grid[y][x] == "E":
            end_pos = (y, x)

def in_grid(pos, grid):
    h, w = len(grid), len(grid[0])
    return not pos[0] < 0 and pos[0] < h and not pos[1] < 0 and pos[1] < w

def print_grid(grid, path):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in path:
                print("O", end="")
            else:
                print(grid[i][j], end="")
        print()  

def move(pos, dir):
    n_pos = (pos[0]+dir[0], pos[1]+dir[1])
    return n_pos

def rotate(dir):
        return (-dir[1], dir[0]), dir, (dir[1], -dir[0])

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

print_grid(grid, set())
print(start_pos, end_pos)


def find_paths(end_pos, grid):
    #print_grid(obstacles, set(), h, w)
    visited = {}
    cost = 0
    to_visit = []
    start_dir = (-1,0)
    heapq.heappush(to_visit, (cost, end_pos))  # Push the starting position with priority 0
    #best_path = set()
    while to_visit:
        cost, curr_pos = heapq.heappop(to_visit)
        if curr_pos in visited:
            continue

        visited[(curr_pos)] = cost
        for dir in DIRS:
            next_pos = move(curr_pos, dir)
            if grid[next_pos[0]][next_pos[1]] == '#':
                continue

            heapq.heappush(to_visit, (cost + 1, next_pos))
    return visited

costs = find_paths(end_pos, grid)
print(costs)
print(len(costs))
default_cost = costs[start_pos]
print(costs[start_pos], costs[end_pos])

def find_cheats(costs, grid, default_cost, ps):
    cheats = {}
    for pos, cost in costs.items():
            for dir in ((i, j) for i in range(-ps, ps+1) for j in range(-ps, ps+1)):
                n_pos = move(pos, dir)
                cheat_duration = sum((abs(a) for a in dir))
                if not n_pos in costs or sum((abs(a) for a in dir)) > ps:
                    continue

                if not n_pos in costs:
                    continue
                saving = costs[n_pos] - cost - cheat_duration - max(0, cost - default_cost)
                if saving > 0:
                    if saving in cheats:
                        cheats[saving] += 1
                    else:
                        cheats[saving] = 1
    return cheats

cheats = find_cheats(costs, grid, default_cost, 2)

print(cheats)

# 1382 Too low
print("Part One : "+ str(sum(v for k, v in cheats.items() if k >= 100)))

cheats = find_cheats(costs, grid, default_cost, 20)

print(cheats)
# 1006101
# 1047015 Too high
print("Part Two : "+ str(sum(v for k, v in cheats.items() if k >= 100)))