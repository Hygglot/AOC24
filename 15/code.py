# Advent of code Year 2024 Day 15 solution
# Author = Hugo Ekinge
# Date = December 2024

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

warehouse, moves = input.split("\n\n")

grid = [[c for c in line.strip()] for line in warehouse.split("\n")]
grid2 = [[c for c in line.strip()] for line in warehouse.split("\n")]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            start_pos = (i, j)
            grid[i][j] = "."
            grid2[i][j] = "."
            break

moves = "".join(moves.split("\n"))

def print_grid(grid, pos):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == pos:
                print("@", end="")
            else:
                print(grid[i][j], end="")
        print()    
    # for row in grid:
    #     print("".join(str(c) for c in row))
    # print(len(grid), len(grid[0]))

def move(pos, dir):
    n_pos = (pos[0]+dir[0], pos[1]+dir[1])
    return n_pos

DIRS = {'>':(0,1), 'v':(1,0), '<':(0,-1), '^':(-1,0)}

def move_robot(pos, dir, grid):
    n_pos = move(pos, DIRS[dir])
    #print(grid[n_pos[0]][n_pos[1]])
    if grid[n_pos[0]][n_pos[1]] == "#":
        return pos, grid
    elif grid[n_pos[0]][n_pos[1]] == ".":
        return n_pos, grid
    elif grid[n_pos[0]][n_pos[1]] == "O":
        first_box = n_pos
        while n_pos := move(n_pos, DIRS[dir]):
            if grid[n_pos[0]][n_pos[1]] != "O":
                break
        #print(grid[n_pos[0]][n_pos[1]], n_pos)
        if grid[n_pos[0]][n_pos[1]] == "#":
            return pos, grid
        elif grid[n_pos[0]][n_pos[1]] == ".":
            grid[first_box[0]][first_box[1]] = "."
            grid[n_pos[0]][n_pos[1]] = "O"
            return first_box, grid
        else:
            print("Error inner")
            
    else:
        print("Error")
        return None
    
def GPS(pos):
    return pos[0]*100+pos[1]

pos = start_pos
print_grid(grid, pos)
print(moves)
print(len(moves))

for dir in moves:
    pos, grid = move_robot(pos, dir, grid)
    #print_grid(grid, pos)

tot = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            tot += GPS((i, j))

print("Part One : "+ str(tot))


def neighbor(pos, ch):
    if ch == "[":
        return (pos[0], pos[1]+1)
    elif ch == "]":
        return (pos[0], pos[1]-1)




def move_robot_2(pos, dir, grid):
    n_pos = move(pos, DIRS[dir])
    n_ch = grid[n_pos[0]][n_pos[1]]

    if n_ch == "#":
        return pos, grid
    elif n_ch == ".":
        return n_pos, grid
    elif n_ch in "[]":
        to_move = []
        to_check = [n_pos, neighbor(n_pos, n_ch)]
        while to_check:
            new = []
            for p in to_check:
                if p in to_move:
                    continue
                n_p = move(p, DIRS[dir])
                n_ch = grid[n_p[0]][n_p[1]]
                if n_ch == "#":
                    return pos, grid
                elif n_ch == ".":
                    to_move.append(p)
                elif n_ch in "[]":
                    to_move.append(p)
                    new.append(n_p)
                    new.append(neighbor(n_p, n_ch))
                else:
                    print("Error inner")
            to_check = new
        edits = {}
        for p in to_move:
            ch = grid[p[0]][p[1]]
            n_p = move(p, DIRS[dir])
            edits[n_p] = ch
            grid[p[0]][p[1]] = "."

        for p, ch in edits.items():
            grid[p[0]][p[1]] = ch

        return n_pos, grid
            
    else:
        print(n_ch)
        print("Error")
        return None

def GPS2(pos, grid):
    # Find the distances to the closes edges of the grid
    ## Completely unneccessary, misread the question
    y, x = pos
    x_min = min(x, len(grid[0]) - x - 2)
    y_min = min(y, len(grid) - y - 1)
    pos_min = x_min, y_min
    print(pos_min)
    return min(pos_min)*100 + max(pos_min)






for i in range(len(grid2)):
    for j in range(len(grid2[0])):
        if grid2[i][j] == "#":
            grid2[i][j] = "##"
        elif grid2[i][j] == ".":
            grid2[i][j] = ".."
        elif grid2[i][j] == "O":
            grid2[i][j] = "[]"
for i in range(len(grid2)):
    grid2[i] = [ch for ch in "".join(grid2[i])]
pos = start_pos[0], start_pos[1]*2
print_grid(grid2, pos)

for dir in moves:
    pos, grid = move_robot_2(pos, dir, grid2)
    # print(dir)
print_grid(grid, pos)


tot = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "[":
            #print(i, j)
            tot += GPS((i, j))



print("Part Two : "+ str(tot))