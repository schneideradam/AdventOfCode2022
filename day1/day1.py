#!/bin/python
 
# O(nLog(n)) time, O(1) space
def solution1():
    maxcals = 0
    sumcals = 0
    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            line = line.strip('\n')
            if line != '':
                sumcals += int(line)
            else:
                maxcals = max(maxcals, sumcals)
                sumcals = 0
    return maxcals

# O(nLog(n)) time, O(n) space
def solution2():
    maxcals = []
    sumcals = 0
    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            line = line.strip('\n')
            if line != '':
                sumcals += int(line)
            else:
                maxcals.append(sumcals)
                sumcals = 0
    return sum(sorted(maxcals, reverse=True)[:3])
       

print(solution1())
print(solution2())