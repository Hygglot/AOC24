# Advent of code Year 2024 Day 2 solution
# Author = Hugo Ekinge
# Date = December 2024

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

rs = [list(map(int, line.split())) for line in input]
safe = 0
sfd = 0

#print(rs)

for r in rs:
    unsafe = False
    #print(r)
    if r == sorted(r) or r == sorted(r, reverse=True):
        p = r[0]
        for i in r[1:]:
            if abs(i-p) > 0 and abs(i-p) < 4:
                p = i
            else:
                unsafe = True
                break
        if not unsafe:
            safe += 1
            print("safe")
            continue
    
    for i in range(len(r)):
        unsafe = False
        rem = r.copy()
        del rem[i]
        #print(rem)
        if rem == sorted(rem) or rem == sorted(rem, reverse=True):
            p = rem[0]
            for i in rem[1:]:
                if abs(i-p) > 0 and abs(i-p) < 4:
                    p = i
                else:
                    unsafe = True
                    break
            if not unsafe:
                sfd += 1
                print("safe with dampener")
                break
    if unsafe:
        print("unsafe")


print("Part One : "+ str(safe))



print("Part Two : "+ str(safe + sfd))