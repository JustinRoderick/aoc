from collections import Counter

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

def part2():
    file = open("input.txt", "r")
    left = []
    right = []
    simularity_score = 0
    for line in file:
        splitted = line.split()
        left.append(int(splitted[0]))
        right.append(int(splitted[1]))
    count = Counter(right)
    for number in left:
        if number in count:
            simularity_score += number * count[number]
    return simularity_score   
    
print(part2())