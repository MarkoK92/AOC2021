with open('inputs/day6.txt') as f:
    data = [int(x) for x in f.read().split(',')]

timer = 9

def Ribe(days):
    r = [data.count(i) for i in range(timer)]
    for i in range(days): 
        r[(i+7) % timer] += r[i % timer] #nova vsakih 7 dni, zanima nas ostanek
    return sum(r)

print(Ribe(80))
print(Ribe(256))

