# Advent of code Year 2024 Day 12 solution
# Author = Hugo Ekinge
# Date = December 2024

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

grid = [[c for c in line.strip()] for line in input]

def in_grid(pos, grid):
    h, w = len(grid), len(grid[0])
    return not pos[0] < 0 and pos[0] < h and not pos[1] < 0 and pos[1] < w

def print_grid(grid):    
    for row in grid:
        print("".join(str(c) for c in row))
    print(len(grid), len(grid[0]))

def move(pos, dir):
    n_pos = (pos[0]+dir[0], pos[1]+dir[1])
    return n_pos

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

print_grid(grid)

visited = set()
components = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (y, x) not in visited:
            component = set()
            letter = grid[y][x]
            to_visit = [(y, x)]
            while to_visit:
                pos = to_visit.pop()
                visited.add(pos)
                component.add(pos)
                for dir in DIRS:
                    new_pos = move(pos, dir)
                    if in_grid(new_pos, grid) and new_pos not in visited and grid[new_pos[0]][new_pos[1]] == letter:
                        to_visit.append(new_pos)
            components.append(component)

print(len(components))

def area(component):
    return len(component)

def perimeter(component):
    per = 0
    for pos in component:
        for dir in DIRS:
            new_pos = move(pos, dir)
            if new_pos not in component:
                per += 1
    return per

cost = 0
for c in components:
    print(area(c), perimeter(c))
    cost += area(c) * perimeter(c)

print("Part One : "+ str(cost))

def perimeter2(component):
    per = 0
    visited = set()
    for pos in component:
        for i, dir in enumerate(DIRS):
            if (pos, dir) in visited:
                continue
            visited.add((pos, dir))
            new_pos = move(pos, dir)
            if new_pos not in component:
                print("Starting new side: ", pos, dir)
                per += 1
                perp1 = DIRS[(i+1)%4]
                perp2 = DIRS[(i+3)%4]
                curr = pos
                while move(curr, perp1) in component and move(move(curr, perp1), dir) not in component:
                    curr = move(curr, perp1)
                    visited.add((curr, dir))
                    print("Perp1: ", curr, perp1)
                curr = pos
                while move(curr, perp2) in component and move(move(curr, perp2), dir) not in component:
                    curr = move(curr, perp2)
                    visited.add((curr, dir))
                    print("Perp2: ", curr)
    return per
    # continuous sides only add 1 to the perimiter, not their total length
    
cost = 0
for c in components:
    print(area(c), perimeter2(c))
    cost += area(c) * perimeter2(c)

print("Part Two : "+ str(cost))