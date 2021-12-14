import re 
from collections import Counter

data = open('inputs/day14.txt').read()

temp = data.split('\n')[0] # split line and take first
polymer  = dict(re.findall(r'(.+) -> (.+)', data)) #regex match ANY char (.) +  1 or more (greedy) repetitions (+), we match first two with last after ->

def pairCount(chars):
    resolution = Counter()
    for n in chars:
        resolution[n[0] + polymer[n]] += chars[n] # create pair for every char
        resolution[polymer[n] + n[1]] += chars[n] # second element of one pair is the first element of the next pair
    return resolution


def Worker(n):
    tempChars = Counter()
    for i in range(len(temp) - 1): # -1 XD
        tempChars[temp[i:i+2]] += 1 #sum iterations by 2 after first process

    for i in range(n):
        tempChars = pairCount(tempChars) #set new pairs

    res = Counter()
    for k in tempChars: #iterate over new pairs
        res[k[0]] += tempChars[k]
    res[temp[-1]] += 1 #only last pair

    element = max(res.values()) - min(res.values()) #subtract most common with least common el
    return element

print(Worker(10)) # first 10
print(Worker(40)) # first 40
