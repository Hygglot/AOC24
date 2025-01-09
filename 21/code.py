# Advent of code Year 2024 Day 21 solution
# Author = Hugo Ekinge
# Date = December 2024

import time

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

codes = [line.strip() for line in input]

codes_ = ["<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
          "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
          "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
          "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
          "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"]

position_numerical = {'A':(0,0), '0':(-1, 0), '1':(-2, 1), '2':(-1, 1), '3':(0, 1), '4':(-2, 2), '5':(-1, 2), '6':(0, 2), '7':(-2, 3), '8':(-1, 3), '9':(0, 3)}
position_directional = {'A':(0,0), '^':(-1, 0), '<':(-2, -1), 'v':(-1, -1), '>':(0, -1)}

def shortest_code(code, position):
    seq = ""
    pos = (0,0)
    # seq_2 = ""
    
    for ch in code:
        target = position[ch]
        right = max(0, target[0]-pos[0])
        left = max(0, pos[0]-target[0])
        up = max(0, target[1]-pos[1])
        down = max(0, pos[1]-target[1])

        if (target[0], pos[1]) == (-2, 0):
            seq += "v"*down + "^"*up
            seq += "<"*left + ">"*right
        elif (pos[0], target[1]) == (-2, 0):
            seq += ">"*right + "<"*left
            seq += "v"*down + "^"*up
        else:
            seq += "<"*left + "v"*down + "^"*up + ">"*right
        seq += 'A'
        pos = target
    
    return seq

def find_shortest(codes, position_numerical, position_directional, chain):
    tot = 0
    for code in codes:
        first = shortest_code(code, position_numerical)
        next = {}
        for chunk in first.split('A')[:-1]:
            if chunk+'A' not in next:
                next[chunk+'A'] = 1
            else:
                next[chunk+'A'] += 1
        
        for i in range(chain):
            #print(next)
            mapping = {}
            new = {}
            for chunk, count in next.items():
                if chunk not in mapping:
                    mapping[chunk] = shortest_code(chunk, position_directional)
                for c in mapping[chunk].split('A')[:-1]:
                    if c+'A' not in new:
                        new[c+'A'] = count
                    else:
                        new[c+'A'] += count
            next = new
            #print(i, sum(v*len(k) for k, v in next.items()), len(next), len(mapping))
        tot += sum(v*len(k) for k, v in next.items())
    return tot

tot = find_shortest(codes, position_numerical, position_directional, 2)


# 251238 Too high
# 238078
print("Part One : "+ str(tot))

tot = find_shortest(codes, position_numerical, position_directional, 25)

# 335879439503508 Too high
# 293919502998014
# 253378763042714 Too low


# 154115708116294 correct in test data
print("Part Two : "+ str(tot))

start = time.time()
tot = find_shortest(codes, position_numerical, position_directional, 10240)
print("Part Three : "+ str(tot))
print(time.time()-start)