# Advent of code Year 2024 Day 13 solution
# Author = Hugo Ekinge
# Date = December 2024

import numpy as np

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

cost_A = 3
cost_B = 1

def parse_machine(block):
    #print(block)
    A, B, prize = block.split("\n")
    A = A.split(": ")[1].split(", ")
    A = (int(A[0][2:]), int(A[1][2:]))
    B = B.split(": ")[1].split(", ")
    B = (int(B[0][2:]), int(B[1][2:]))
    prize = prize.split(": ")[1].split(", ")
    prize = (int(prize[0][2:]), int(prize[1][2:]))

    #print(A, B, prize)
    return A, B, prize
    

def get_cost(A, B, prize):
    # Cramer's rule manually
    Ax, Ay = A
    Bx, By = B
    Px, Py = prize

    det = Ax*By - Ay*Bx
    A_press = (By * Px - Bx * Py) // det
    B_press = (Ax * Py - Px * Ay) // det

    
    if Ax * A_press + Bx * B_press == Px and Ay * A_press + By * B_press == Py:
        return A_press * cost_A + B_press * cost_B
    else:
        return 0

    # Numpy with rounding for integer solutions
    # Create the coefficient matrix and the constants vector
    coefficients = np.array([[Ax, Bx], [Ay, By]]) # Order important!
    constants = np.array([Px, Py])

    # Solve the system of linear equations
    A_presses, B_presses = np.linalg.solve(coefficients, constants)

    # Check if the solution is an integer
    if np.isclose(A_presses, round(A_presses), rtol=1.e-15) and np.isclose(B_presses, round(B_presses), rtol=1.e-15):
        A_presses = int(round(A_presses))
        B_presses = int(round(B_presses))
        #print(A_presses, B_presses)
        cost = A_presses * cost_A + B_presses * cost_B
    else:
        cost = 0
    return cost

machines = []
for block in input.split("\n\n"):
    A, B, prize = parse_machine(block)
    machines.append((A, B, prize))

cost = 0
for machine in machines:
    cost += get_cost(*machine)

print("Part One : "+ str(cost))

offset = 10000000000000
machines_offset = []
for block in input.split("\n\n"):
    A, B, prize = parse_machine(block)
    prize = (p + offset for p in prize)
    machines_offset.append((A, B, prize))

cost = 0
for machine in machines_offset:
    cost += get_cost(*machine)

# 163992009892954 too high
# 108528956728655 right
# 80835062124714 too low
print("Part Two : "+ str(cost))