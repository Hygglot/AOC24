import time

# Advent of code Year 2024 Day 19 solution
# Author = Hugo Ekinge
# Date = December 2024

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

patterns, designs = input.split("\n\n")

patterns = patterns.split(", ")
designs = designs.split("\n")

#print(len(patterns))
#print(designs)

tot = 0
for design in designs:
    to_test = [design]
    while to_test:
        des = to_test.pop()
        if not des:
            tot += 1
            break
        for pat in patterns:
            if des.startswith(pat):
                to_test.append(des[len(pat):])

print("Part One : "+ str(tot))

start_time = time.time()

patterns_list = []
for design in designs:
    filtered_patterns = []
    for pattern in patterns:
        if pattern in design:
            filtered_patterns.append(pattern)
    patterns_list.append(filtered_patterns)

#print(patterns_list)

tot = 0
for design, patterns in zip(designs, patterns_list):
    to_test = {design: 1}
    while to_test:
        des, count = to_test.popitem()
        #print(des, count)
        if not des:
            #print("Match found: ", design, count)
            tot += count
            continue

        for pat in patterns:
            if des.startswith(pat):
                n_res = des[len(pat):]
                if n_res in to_test:
                    to_test[n_res] += count
                else:
                    to_test[n_res] = count

        to_test = dict(sorted(to_test.items(), key=lambda x: len(x[0]), reverse=False))

print("Part Two : "+ str(tot))

end_time = time.time()
print("Execution Time: {:.2f} seconds".format(end_time - start_time))