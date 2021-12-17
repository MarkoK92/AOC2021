mina, maxa, minb, maxb = 14, 50, -267, -225

# The probe's x position increases by its x velocity.
# The probe's y position increases by its y velocity.
# Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
# Due to gravity, the probe's y velocity decreases by 1.

points = []
highb = 0
vels = set()

for a in range(0, maxa + 1):
    x = 0
    points.append([0] + [x := x + dx for dx in range(a, 0, -1)])

for b in range(minb, -minb):
    pointB = 0
    indexB = b
    topy = 0
    num = 0
    while pointB >= minb:
        if pointB <= maxb:
            for a in range(0, maxa + 1):
                if mina <= points[a][min(num, len(points[a]) - 1)] <= maxa:
                   highb = max(highb, topy)
                   vels.add((a, b))
        pointB += indexB
        if indexB == 0:
            topy = pointB
        indexB -= 1
        num += 1

print(highb) #highest b trajectory
print(len(vels)) #count velocity vals
