# Advent of code Year 2024 Day 9 solution
# Author = Hugo Ekinge
# Date = December 2023

from tqdm import tqdm

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [int(ch) for ch in input.strip()]
n_files = len(input)//2 +1

files = [0] * n_files
disk_addr = 0
empty = []
print(len(input))
print(len(files))
for i, num in enumerate(input):
    if i % 2 == 0:
        files[i//2] = num
    else:
        empty.append(num)
    disk_addr += num

compact = [0] * sum(files)

print(files)
print(empty)
print(len(files))
fc = files.copy()

print(len(compact))


c_i = 0
b = False
for (f, l), empt in zip(enumerate(files), empty):
    for i in range(c_i, c_i + l):
        if i < len(compact):
            compact[i] = f
        else:
            b = True
            break
    if b:
        break
    c_i += l
    for i in range(c_i, c_i + empt):
        for j in range(len(files) - 1, -1, -1):
            if files[j] > 0:
                files[j] -= 1
                break
        if i < len(compact):
            compact[i] = j
        else:  
            b = True
            break
    c_i += empt
    if b:
        break
        

print(c_i)
print(compact)
    
    
checksum = sum(index * value for index, value in enumerate(compact))


print("Part One : "+ str(checksum))


# input
files = fc.copy()
compact = [0] * sum(input)

n_files = len(input)//2 +1

files = [(0,0,0)] * n_files
disk_addr = 0
empty = []
print(len(input))
print(len(files))
disk_addr = 0
for i, num in enumerate(input):
    if i % 2 == 0:
        files[i//2] = (disk_addr, num, i//2)
    else:
        if num > 0:
            empty.append((disk_addr, num))
    disk_addr += num

# print(files)
# print(empty)
# print(len(files))
fc = files.copy()

print(len(compact))
print(fc)
print(empty)

for file in tqdm(reversed(files), total=len(files), disable=False):
    addr, length, index = file
    left_emtpy = addr
    left_length = 0
    found = False
    for empty_addr, empty_length in empty:
        #print(length, empty_length)
        if empty_length >= length and empty_addr < left_emtpy:
            found = True
            left_emtpy = empty_addr
            left_length = empty_length

    if not found:
        continue
    empty_addr, empty_length = left_emtpy, left_length
    #print("Found empty space: ", empty_addr, empty_length)
    fc.remove(file)
    fc.append((empty_addr, length, index))
    empty.remove((empty_addr, empty_length))
    if empty_length-length > 0:
        empty.append((empty_addr+length, empty_length-length))
    
    # if empty space to left or right, merge them together
    for empty_addr2, empty_length2 in empty.copy():
        if empty_addr2 == addr+length:
            empty.remove((empty_addr2, empty_length2))
            length += empty_length2
        if empty_addr2+empty_length2 == addr:
            empty.remove((empty_addr2, empty_length2))
            length += empty_length2
            addr = empty_addr2
    empty.append((addr, length))

    continue

    cc = compact.copy()
    for addr, l, index in fc:
        for i in range(addr, addr + l):
            cc[i] = index
        
    print(''.join(str(c) if c != 0 else '.' for c in cc))
    print(empty)

    # print(fc)
    # print(empty)

cc = compact.copy()
for addr, l, index in fc:
    for i in range(addr, addr + l):
        cc[i] = index
    
print(''.join(str(c) for c in cc))

checksum = sum(index * value for index, value in enumerate(cc))


# 6415090760884 too high
print("Part Two : "+ str(checksum))