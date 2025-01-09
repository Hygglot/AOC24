# Advent of code Year 2024 Day 23 solution
# Author = Hugo Ekinge
# Date = December 2024
from itertools import combinations
from tqdm import tqdm

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def connected(graph, nodes):
    for n1, n2 in combinations(nodes, 2):
        if n2 not in graph[n1]:
            return False
    return True

connections = [line.split('-') for line in input.split('\n')]
#print(connections)
computers = {}
for a, b in connections:
    if a not in computers:
        computers[a] = {b}
    else:
        computers[a].add(b)
    if b not in computers:
        computers[b] = {a}
    else:
        computers[b].add(a)

#print(computers, len(computers))

tot = 0
tested = set()
for comp in tqdm(computers, total=len(computers)):
    for comb in combinations(computers[comp], 2):
        if any(c in tested for c in comb):
            continue
        if connected(computers, comb):
            if any(c[0] == 't' for c in comb) or comp[0] == 't':
                tot += 1
    tested.add(comp)

print("Part One : "+ str(tot))

start = 1
for l in range(start, len(computers['jm'])+1):
    tot = 0
    tested = set()
    for comp in computers:
        for comb in combinations(computers[comp], l):
            if any(c in tested for c in comb):
                continue
            if connected(computers, comb):
                tot += 1
                group = [comp, *comb]
        tested.add(comp)
    print(l+1, tot)

print("Part Two : "+ str(','.join(sorted(group))))