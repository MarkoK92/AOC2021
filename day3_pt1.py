import sys

data = open('inputs/day3.txt').read().splitlines()

gamma= '' 
epsilon = ''

for _ in range(len(data[0])):
        b1 = sum(n[_] == '0' for n in data)
        b2 = sum(n[_] == '1' for n in data)
        gamma += '0' if b1 > b2 else '1'
        epsilon += '1' if b1 > b2 else '0'

pwr = int(gamma, 2) * int(epsilon, 2)

print(pwr)
