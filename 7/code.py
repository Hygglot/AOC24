# Advent of code Year 2024 Day 7 solution
# Author = Hugo Ekinge
# Date = December 2023

from itertools import product

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

def plus(a, b):
    return a + b

def mult(a, b):
    return a * b

def con(a, b):
    return int(str(a) + str(b))

ops = [mult, plus]
ops2 = [mult, con, plus]

tot = 0
max = 0
for line in input:
    val, nums = line.split(':')
    val = int(val)
    nums = list(map(int, nums.split()))
    print(nums)
    # if len(nums) > max:
    #     max = len(nums)
    for perm in product(ops, repeat=len(nums)-1):
        res = nums[0]
        #print(perm)
        for i, op in enumerate(perm):
            res = op(res, nums[i+1])
            if res > val:
                break
        if res == val:
            tot += val
            print("WORKS")
            break

tot2 = 0
for line in input:
    val, nums = line.split(':')
    val = int(val)
    nums = list(map(int, nums.split()))
    for perm in product(ops2, repeat=len(nums)-1):
        res = nums[0]
        #print(perm)
        for i, op in enumerate(perm):
            res = op(res, nums[i+1])
            if res > val:
                break
        if res == val:
            tot2 += val
            print("WORKS")
            break

# 850435817339
print("Part One : "+ str(tot))



print("Part Two : "+ str(tot2))