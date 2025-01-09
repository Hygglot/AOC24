# Advent of code Year 2024 Day 16 solution
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
visited = set()

cost = 0
to_visit = []
start_dir = (0,1)
heapq.heappush(to_visit, (cost, start_pos, start_dir))  # Push the starting position with priority 0

while to_visit:

    cost, curr_pos, curr_dir = heapq.heappop(to_visit)
    if curr_pos in visited:
        continue
    elif grid[curr_pos[0]][curr_pos[1]] == "E":
            print(cost)
            break
    visited.add(curr_pos)
    
    for dir in rotate(curr_dir):
        next_pos = move(curr_pos, dir)
        if grid[next_pos[0]][next_pos[1]] == "#":
            continue
        
        if dir == curr_dir:
            heapq.heappush(to_visit, (cost + 1, next_pos, dir))
        else:
            heapq.heappush(to_visit, (cost + 1001, next_pos, dir))


# 83431 Too low
# 83432 Right

print("Part One : "+ str(cost))

visited = {}

cost = 0
to_visit = []
start_dir = (0,1)
heapq.heappush(to_visit, (cost, start_pos, start_dir, set()))  # Push the starting position with priority 0
best_paths = set()
best_cost = float('inf')
while to_visit:

    cost, curr_pos, curr_dir, path = heapq.heappop(to_visit)
    if (curr_pos, curr_dir) in visited:
        if cost > visited[(curr_pos, curr_dir)]:
            continue
    if cost > best_cost:
        break

    curr_path = path.copy()
    curr_path.add(curr_pos)

    print(cost)

    if grid[curr_pos[0]][curr_pos[1]] == "E":
            print(cost)
            #print(visited)
            if cost < best_cost:
                print("Found first path!", len(curr_path))
                best_cost = cost
                best_paths = curr_path
                #print(to_visit, len(to_visit))
            elif cost == best_cost:
                print("Found another path!", len(curr_path))
                best_paths.update(curr_path)
            else:
                break
            continue

    visited[(curr_pos, curr_dir)] = cost
    
    
    for dir in rotate(curr_dir):
        next_pos = move(curr_pos, dir)
        if grid[next_pos[0]][next_pos[1]] == "#":
            continue

        if dir == curr_dir:
            heapq.heappush(to_visit, (cost + 1, next_pos, dir, curr_path))
        else:
            heapq.heappush(to_visit, (cost + 1001, next_pos, dir, curr_path))

print_grid(grid, best_paths)


# 433 Too low
# 467 Right
print("Part Two : "+ str(len(best_paths)))