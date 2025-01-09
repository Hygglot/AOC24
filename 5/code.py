# Advent of code Year 2024 Day 5 solution
# Author = Hugo Ekinge
# Date = December 2023

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

rules, updates = input.split("\n\n")
rs = {}
for rule in rules.split("\n"):
    k, v = map(int, rule.split("|"))
    if k not in rs:
        rs[k] = []
    rs[k].append(v)

print(rs)

tot = 0
tot2 = 0
moves = 0

for update in updates.split("\n"):
    ps = list(map(int, update.split(',')))
    v = True
    for i, p in enumerate(ps):
        if p in rs:
            if any([x in ps[:i] for x in rs[p]]):
                v = False
                break
    if v:
        #print(ps)
        tot += ps[(len(ps)-1)//2]
    else:
        solved = False
        while not solved:
            solved = True
            for i, p in enumerate(ps):
                if p in rs:
                    wrongs = [x for x in rs[p] if x in ps[:i]]
                    if not wrongs:
                        continue
                    solved = False
                    #print(f"Wrong: {wrongs}")
                    moves += len(wrongs)
                    for wrong in wrongs:
                        ps.remove(wrong)
                    ps.extend(wrongs)
                    break
                        

        print(ps)
        tot2 += ps[(len(ps)-1)//2]

print(moves)    

#4462
print("Part One : "+ str(tot))

#6767
print("Part Two : "+ str(tot2))