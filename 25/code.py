# Advent of code Year 2024 Day 25 solution
# Author = Hugo Ekinge
# Date = December 2024

from itertools import product

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = input.split('\n\n')

locks = []
keys = []
for block in input:
    #print(block)
    lines = block.split('\n')
    if lines[0] == '#'*5:
        lock = lines[1:]
        lock_profle = []
        for pos in range(5):
            for h in range(6):
                if lock[h][pos] == '.':
                    lock_profle.append(h)
                    break
        locks.append(lock_profle)
        #print(lock_profle)
                    

    elif lines[-1] == '#'*5:
        key = lines[:-1]
        key_profle = []
        for pos in range(5):
            for h in range(5, -1, -1):
                if key[h][pos] == '.':
                    key_profle.append(5-h)
                    break
        keys.append(key_profle)
        #print(key_profle)

print(len(locks))
print(len(keys))

from itertools import product

tot = 0
for key, lock in product(keys, locks):
    #print(key, lock)
    if not any(k+l >5 for k, l in zip(key, lock)):
        tot += 1


print("Part One : "+ str(tot))


# No part 2, last day of the calendar
print("Part Two : "+ str(None))