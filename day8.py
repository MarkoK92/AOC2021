from collections import Counter

mapper = {}
first = []
second = []

with open('inputs/day8.txt') as f:
    data = [x.split("|") for x in f]

pattern = "abcefg cf acdeg acdfg bdcf abdfg abdefg acf abcdefg abcdfg"
numbers = Counter(list(pattern.replace(" ", ""))) #map chars to numbers

for num, char in enumerate(pattern.split(" ")):
    mapper[tuple(sorted([numbers[c] for c in char]))] = num #map pattern chars with numbers and count how many match

for d in data:
    signalPattern = Counter(list(d[0].replace(" ", "")))
    outVal = d[1].strip()
    op = [mapper[tuple(sorted([signalPattern[v] for v in v]))] for v in outVal.split(" ")] 

    first.append(len([m for m in op if m in [1, 4, 7, 8]]))   
    second.append(int("".join([str(x) for x in op])))

print(sum(first))
print(sum(second))
