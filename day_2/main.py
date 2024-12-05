def is_safe(report):
    is_increasing = all(report[i+1] - report[i] >= 1 and report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    is_decreasing = all(report[i] - report[i+1] >= 1 and report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return is_increasing or is_decreasing

def part1():
    file = open("input.txt", "r")
    count = 0
    for line in file:
        report = list(map(int, line.strip().split()))
        if is_safe(report):
            count += 1
            continue
    
    return count 

print(part1())

def part2():
    file = open("input.txt", "r")
    count = 0
    for line in file:
        report = list(map(int, line.strip().split()))
        if is_safe(report):
            count += 1
            continue
        else:
            for i in range(len(report)):
               if(is_safe(report[:i] + report[i+1:])):
                   count += 1
                   break
    
    return count

print(part2())