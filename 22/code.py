# Advent of code Year 2024 Day 22 solution
# Author = Hugo Ekinge
# Date = December 2024

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [int(line) for line in input.split('\n')]

def mix(val, secret):
    # Bitwise XOR
    return val ^ secret

def prune(secret):
    return secret % 2**24

tot = 0
for secret in input:
    for i in range(2000):
        secret = mix(secret* 2**6, secret)
        secret = prune(secret)
        
        secret = mix(secret// 2**5, secret)
        secret = prune(secret)

        secret = mix(secret* 2**11, secret)
        secret = prune(secret)

    tot += secret

print("Part One : "+ str(tot))


def price(secret):
    return secret % 10

tot = 0
pattern_dicts = []
for secret in input:
    p_dict = {}
    changes = ()
    p = price(secret)
    for i in range(2000):
        secret = mix(secret* 2**6, secret)
        secret = prune(secret)
        
        secret = mix(secret// 2**5, secret)
        secret = prune(secret)

        secret = mix(secret* 2**11, secret)
        secret = prune(secret)

        np = price(secret)
        dp = np - p
        p = np
        #print(np, dp)
        changes = (*changes[-3:], dp)
        if changes not in p_dict and len(changes) == 4:
            p_dict[changes] = np
    #print(len(p_dict))
    pattern_dicts.append(p_dict)

print(sum(len(p) for p in pattern_dicts))
# Make 1 single dict of all the dicts in pattern_dicts 
combined = set()
for p_dict in pattern_dicts:
    for key in p_dict:
        if key not in combined:
            combined.add(key)
print(len(combined))

max = 0
for key in combined:
    tot = 0
    for p_dict in pattern_dicts:
        if key in p_dict:
            tot += p_dict[key]
    if tot > max:
        max = tot
        print("New max: ", max, key)

# 1657 Too low

print("Part Two : "+ str(max))