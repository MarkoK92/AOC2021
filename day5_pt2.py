from collections import defaultdict

dict = []
sticisce = 0
pts = defaultdict(int)

with open('inputs/day5.txt') as data:
    for d in data.readlines():
        split = d.strip().split('->')
        dict.append([
        [int(n) for n in split[0].split(',')],
        [int(n) for n in split[1].split(',')]
        ])

for (x1, y1), (x2, y2) in dict:
    if x1 == x2:
        for y in range(min(y1, y2), max(y1,y2) + 1):
            pts[x1, y] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            pts[x, y1] += 1
    else:
        dx = -1 if x1 > x2 else 1
        dy = -1 if y1 > y2 else 1
 
        while x1 != x2:
            pts[x1, y1] += 1
            x1 += dx
            y1 += dy
 
        pts[x1, y1] += 1

for x, y in pts:
    if pts[x, y] > 1:
        sticisce += 1
 
print(sticisce)


