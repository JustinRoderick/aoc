# Day 1 solutions for part 1 and 2
def part1():
    file = open("input.txt", "r")
    left = []
    right = []
    total = 0
    for line in file:
        splitted = line.split()
        left.append(int(splitted[0]))
        right.append(int(splitted[1]))
    left.sort()
    right.sort()
    for i in range(len(left)):
        total += abs(left[i] - right[i])        
    return total

print(part1())