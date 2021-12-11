

import statistics

with open("inputs/day10.txt") as fh:
    data = [line.strip() for line in fh.readlines()]

separators = {'(': ')', '[': ']', '{': '}', '<': '>'}
medianList = []
table = []
errosList= []

for line in data:
    for separator in line:
        if separator in separators.keys(): 
            table.append(separators[separator]) #add if matching
        elif separator == table[-1]: #remove last element from list
            table.pop()
        else:
            errosList.append({')': 3, ']': 57, '}': 1197, '>': 25137}[separator]) #match separator to number
            break 
    else:
        sc = 0
        while table: 
            sc = sc * 5 + {')': 1, ']': 2, '}': 3, '>': 4}[table.pop()] #replace chars with nums and multiply by 5
        if sc > 0:
            medianList.append(sc)

print(sum(errosList))
print(statistics.median(medianList))
