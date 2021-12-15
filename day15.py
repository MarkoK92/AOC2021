import heapq

cave = [list(map(int, list(d))) for d in open('inputs/day15.txt').read().splitlines()]

def lowestRisk(cave):
    a = len(cave)
    b = len(cave[0]) # need to split data to
    rlevels = [[-1]*a for i in range(a)] # take only last 
    rlevels[0][0] = 0
    paths = [(0, 0, 0)]
    while rlevels[-1][-1] == -1: # iterate from botton to top
        level, row, col = heapq.heappop(paths) #take out the smallest path
        for rowIndex, colIndex in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # map risk patterns 
            rowNum, colNum = row + rowIndex, col + colIndex #iterate by indexes
            if 0 <= rowNum < a and 0 <= colNum < b and rlevels[rowNum][colNum] == -1: #check if the numbers match initial value paths
                rlevels[rowNum][colNum] = level + cave[rowNum][colNum] # if so assign them as new risk level
                heapq.heappush(paths, (rlevels[rowNum][colNum], rowNum, colNum)) #push to risk levels
    return rlevels[-1][-1] # we only want the lowest risk of them all

def largerCave(cave):
    a = len(cave)
    b = len(cave[0])
    rlevel = [[0] * (5 * b) for _ in range(5 * a)] # 5 times larger than before
    for row5 in range(5):
        for col5 in range(5):
            for row in range(a):
                for col in range(b):
                    nr, nc = a * row5 + row, b * col5 + col #iterate by indexes
                    rlevel[nr][nc] = cave[row][col] + row5 + col5 # assign them as new risk level
                    if rlevel[nr][nc] > 9: # if risk levels above 9 wrap back around to 1
                        rlevel[nr][nc] -= 9
    return rlevel

print(lowestRisk(cave))
print(lowestRisk(largerCave(cave)))



