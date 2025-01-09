# Advent of code Year 2024 Day 17 solution
# Author = Hugo Ekinge
# Date = December 2024

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    
regs, prog = input.split('\n\n')
regs = {reg: int(num.split(': ')[-1]) for reg, num in zip('ABC', regs.split('\n'))}
prog = [int(num) for num in prog.split(': ')[-1].split(',')]

print(regs)
print(prog)
reg2 = regs.copy()

def combo(op, regs):
    if op >= 0 and op <= 3:
        return op
    elif op == 4:
        return regs['A']
    elif op == 5:
        return regs['B']
    elif op == 6:
        return regs['C']
    elif op == 7:
        raise Exception('Invalid operation')

def simulate(prog, regs):
    output = []
    ptr = 0
    while ptr +1 < len(prog):
        instr = prog[ptr]
        operand = prog[ptr+1]
        if instr == 0:   # adv
            regs['A'] //= 2**combo(operand, regs)
        elif instr == 1: # bxl
            regs['B'] ^= operand
        elif instr == 2: # bst
            regs['B'] = combo(operand, regs) % 8
        elif instr == 3: # jnz
            if regs['A']:
                ptr = operand
                continue
        elif instr == 4: # bxc
            regs['B'] ^= regs['C']
        elif instr == 5: # out
            output.append(combo(operand, regs) % 8)
        elif instr == 6: # bdv
            regs['B'] = regs['A'] // 2**combo(operand, regs)
        elif instr == 7: # cdv
            regs['C'] = regs['A'] // 2**combo(operand, regs)
        ptr += 2
    return output

output = simulate(prog, regs)
    
ans = ','.join(map(str, output))

print("Part One : "+ str(ans))


A_strings = ['']
for i in reversed(range(len(prog))):
    desired = prog[i:]
    print(f'{i}: {desired}')
    n_A_strings = []
    for A_string in A_strings:
        for num in range(8):
            num_bin = bin(num)[2:].zfill(3)
            test_A = A_string + num_bin
            test_out = simulate(prog, {'A': int(test_A, 2), 'B': 0, 'C': 0})
            if test_out == desired:
                print(f'Sucess! {test_out}, {num_bin}')
                n_A_strings.append(A_string + num_bin)
    A_strings = n_A_strings
        
# 106086383298970 Too high
print(A_strings)
print(list(int(A_string, 2) for A_string in A_strings)) 
print(int(A_strings[0], 2))
print(sorted(list(int(A_string, 2) for A_string in A_strings)) == list(int(A_string, 2) for A_string in A_strings))

# 2 4 regs['B'] = regs['A'] % 8
# 1 5 regs['B'] ^= 101
# 7 5 regs['C'] = regs['A'] // 2**regs['B']
# 1 6 regs['B'] ^= 110
# 0 3 regs['A'] //= 2**3
# 4 2 regs['B'] ^= regs['C']
# 5 5 output.append(regs['B'] % 8)
# 3 0 if regs['A']: ptr = 0


print("Part Two : "+ str(int(A_strings[0], 2)))