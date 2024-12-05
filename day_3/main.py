import numpy as np
import re

def part1():
    file = open("input.txt", "r")
    total = 0
    string = file.read()
    found = re.findall("mul\(\d+,\d+\)", string)
    
    for i in found:
        a, b = map(int, re.findall("\d+", i))
        total += a * b
    return total

print(part1())

def part2():
    file = open("input.txt", "r")
    
    
print(part2())