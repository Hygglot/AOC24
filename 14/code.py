# Advent of code Year 2024 Day 14 solution
# Author = Hugo Ekinge
# Date = December 2024

def print_grid(h, w, pos):
    grid = [['.' for x in range(w)] for y in range(h)]
    for p in pos:
        if grid[p[1]][p[0]] == '.':
            grid[p[1]][p[0]] = 1
        else:
            grid[p[1]][p[0]] += 1
    for row in grid:
        print("".join(str(c) for c in row))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    inp = input_file.readlines()

rs = []
for line in inp:
    p, v = line.strip().split(" ")
    p = tuple(int(num) for num in p[2:].split(","))
    v = tuple(int(num) for num in v[2:].split(","))
    #print(p, v)
    rs.append((p, v))

w = 101
h = 103
time = 100
after = []
for r in rs:
    #print(r)
    px, py = r[0]
    vx, vy = r[1]
    npx, npy = px+(w+vx)*time, py+(h+vy)*time
    npx %= w
    npy %= h
    after.append((npx, npy))

print(after)
print_grid(h, w, after)

def danger_score(after):
    q1 = q2 = q3 = q4 = other = 0
    for r in after:
        px, py = r
        if px < w//2 and py < h//2:
            q1 += 1
        elif px > w//2 and py < h//2:
            q2 += 1
        elif px < w//2 and py > h//2:
            q3 += 1
        elif px > w//2 and py > h//2:
            q4 += 1
        else:
            other += 1
    return q1 * q2 * q3 * q4

# 225943500
# 224264192 Too low
print("Part One : "+ str(danger_score(after)))

time = 1000000
start = 1
lowerst_danger = float("inf")
for t in range(start, start + time):
    after = []
    for r in rs:
        #print(r)
        px, py = r[0]
        vx, vy = r[1]
        npx, npy = px+(w+vx)*t, py+(h+vy)*t
        npx %= w
        npy %= h
        after.append((npx, npy))
    d = danger_score(after)
    if d < lowerst_danger:
        lowerst_danger = d
        print_grid(h, w, after)
        print(t, d)
        input("Press Enter to continue...")

print("Part Two : "+ str(None))