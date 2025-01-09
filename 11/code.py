# Advent of code Year 2024 Day 11 solution
# Author = Hugo Ekinge
# Date = December 2024

from tqdm import tqdm

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

stones = [int(ch) for ch in input.strip().split()]
stone_dict = {}
for stone in stones:
    if stone not in stone_dict:
        stone_dict[stone] = 1
    else:
        stone_dict[stone] += 1
print(stones)
print(stone_dict)

def blink(stones):
    new = []
    for stone in stones:
        if stone == 0:
            new.append(1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            new.append(int(stone[:len(stone)//2]))
            new.append(int(stone[len(stone)//2:]))
        else:
            new.append(stone*2024)
    return new

def blink_dict(stone_dict):
    new = {}
    for stone in stone_dict:
        if stone == 0:
            if 1 not in new:
                new[1] = stone_dict[stone]
            else:
                new[1] += stone_dict[stone]
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            left = int(s[:len(s)//2])
            right = int(s[len(s)//2:])

            if left not in new:
                new[left] = stone_dict[stone]
            else:
                new[left] += stone_dict[stone]

            if right not in new:
                new[right] = stone_dict[stone]
            else:
                new[right] += stone_dict[stone]
        else:
            if stone*2024 not in new:
                new[stone*2024] = stone_dict[stone]
            else:
                new[stone*2024] += stone_dict[stone]
    return new

for i in tqdm(range(25), total=5, disable=True):
    stones = blink(stones)
    print(len(stones))
    #print(stones)

for i in tqdm(range(750), total=5, disable=True):
    stone_dict = blink_dict(stone_dict)
    print(sum(stone_dict.values()), len(stone_dict))


print("Part One : "+ str(len(stones)))



print("Part Two : "+ str(sum(stone_dict.values())))