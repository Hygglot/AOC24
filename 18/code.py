# Advent of code Year 2024 Day 18 solution
# Author = Hugo Ekinge
# Date = December 2024

import heapq

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    in_data = input_file.read()

def in_grid(pos, h, w):
    #h, w = len(grid), len(grid[0])
    return not pos[0] < 0 and pos[0] < h and not pos[1] < 0 and pos[1] < w

def print_grid(obstacles, path, h, w):    
    for i in range(h):
        for j in range(w):
            if (j, i) in path:
                print("O", end="")
            elif (j, i) in obstacles:
                print("#", end="")
            else:
                print('.', end="")
        print()  

def move(pos, dir):
    n_pos = (pos[0]+dir[0], pos[1]+dir[1])
    return n_pos

def rotate(dir):
        return (-dir[1], dir[0]), dir, (dir[1], -dir[0])

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

coords = [tuple(map(int, line.split(","))) for line in in_data.split("\n")]
#print(coords)

w = h = 71
time = 1024
obstacles = set(coords[:time])

start_pos = (0, 0)
end_pos = (h-1, w-1)

def find_path(start_pos, end_pos, obstacles, h, w):
    #print_grid(obstacles, set(), h, w)
    visited = {}
    cost = 0
    to_visit = []
    start_dir = (0,1)
    heapq.heappush(to_visit, (cost, start_pos, start_dir, set()))  # Push the starting position with priority 0
    best_path = set()
    while to_visit:
        cost, curr_pos, curr_dir, path = heapq.heappop(to_visit)
        if curr_pos in visited:
            continue

        curr_path = path.copy()
        curr_path.add(curr_pos)
        #print(cost)
        if curr_pos == end_pos:
                # print(cost)
                # print(visited)
                # print_grid(obstacles, curr_path, h, w)
                #print("Found first path!", len(curr_path))
                #print(curr_path)
                best_path = curr_path
                #print(to_visit, len(to_visit))
                break

        visited[(curr_pos)] = cost
        #print_grid(obstacles, curr_path, h, w)
        #print(len(visited))
        
        for dir in rotate(curr_dir):
            next_pos = move(curr_pos, dir)
            if next_pos in obstacles or not in_grid(next_pos, h, w):
                continue

            heapq.heappush(to_visit, (cost + 1, next_pos, dir, curr_path))
    return best_path

best_path = find_path(start_pos, end_pos, obstacles, h, w)
print_grid(obstacles, best_path, h, w)

# 273 too high
print("Part One : "+ str(len(best_path)-1))

for i in range(time, len(coords)):
    print(i)
    new_obs = coords[i]
    obstacles.add(new_obs)
    if new_obs not in  best_path:
        continue

    best_path = find_path(start_pos, end_pos, obstacles, h, w)
    if not best_path:
        print("No path found")
        break

ans = ','.join(map(str,coords[i]))
print("Part Two : "+ str(ans))