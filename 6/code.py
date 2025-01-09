# Advent of code Year 2024 Day 6 solution
# Author = Hugo Ekinge
# Date = December 2023

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    
grid = [[ch for ch in line] for line in input.split()]
obs = set()
visited = set()

def move(pos, dir):
    y, x = pos
    if dir == 0:
        return (y-1, x)
    elif dir == 1:  
        return (y, x+1)
    elif dir == 2:
        return (y+1, x)
    elif dir == 3:
        return (y, x-1)
    
def turn_right(dir):
    return (dir + 1) % 4

def in_grid(pos):
    y, x = pos
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

def print_grid(grid):
    for line in grid:
        print(''.join(line))

print(grid)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == '#':
            obs.add((y, x))
        elif grid[y][x] == '^':
            start_pos = (y, x)
            dir = 0
            visited.add(start_pos)
            
print(len(obs))

pos = start_pos
while in_grid(pos):
    visited.add(pos)
    if move(pos, dir) in obs:
        dir = turn_right(dir)
        continue
    pos = move(pos, dir)
    
print_grid(grid)
    
p_obs = visited.copy()
p_obs.remove(start_pos)

print("Part One : "+ str(len(visited)))


tot = 0
for ob in p_obs:
    n_obs = obs.copy()
    n_obs.add(ob)
    pos, dir = start_pos, 0
    visited = set()
    while in_grid(pos):
        if (pos, dir) in visited:
            tot += 1
            if tot % 1000 == 0:
                print(tot)
            #print(tot)
            break
        visited.add((pos, dir))
        if move(pos, dir) in n_obs:
            dir = turn_right(dir)
            continue
        pos = move(pos, dir)

print("Part Two : "+ str(tot))