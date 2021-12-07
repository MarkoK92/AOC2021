import statistics
import math 

with open('inputs/day7.txt') as f:
    data = [int(x) for x in f.read().split(',')]

mediana = math.trunc(statistics.median(data)) #only whole nums
average = math.trunc(statistics.mean(data)) #only whole nums

fuel = [abs(p-mediana) for p in data] #cant have negative

def FuelDistance(step, avg):
    dist = abs(step-avg) #cant have negative
    f = [x for x in range(dist+1)]
    return f

AlignFirst = [sum(FuelDistance(step, average)) for step in data]
AlignSecond = [sum(FuelDistance(step, average+1)) for step in data] #next step

print(sum(fuel))
print(min(sum(AlignFirst), sum(AlignSecond)))
