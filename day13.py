data = open('inputs/day13.txt').read().splitlines()

setPoints = set()
overlaps = []

#prepare data
for d in data: 
    if ',' in d:
        (r1, r2) = d.split(',') #(x, y)
        setPoints.add((int(r1), int(r2)))
    if d.startswith('fold'):
        (x, num) = d.split()[-1].split('=') #split last string with = and assign axys + num
        overlaps.append((x, int(num)))

def overlap(pts, overlaps):
    for x, num in overlaps:
        overlaped = set()
        for a, b in pts:
            if x == 'x':
                overlaped.add((a 
                if a < num 
                else 2 * num - a, b)) 
            else:
                overlaped.add((a, b 
                if b < num 
                else 2 * num - b))
        pts = overlaped # set to current setPoints
    return pts

visiblepoints = overlap(setPoints, overlaps[:1]) #only first overlap
print(len(visiblepoints)) 

overlaped = overlap(setPoints, overlaps)

maxa = max(a for a, i in overlaped) #get max a point
maxb = max(b for i, b in overlaped) #get max b point

image = [[' '] * (maxa + 1) for _ in range(maxb + 1)] # set up IR image with max a,b values
for a, b in overlaped: image[b][a] = 'X' #replace a,b overlaped points with X

print('\n'.join(''.join(x) for x in image)) # concatenate and split new line for every x