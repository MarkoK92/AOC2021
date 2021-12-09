
import heapq
import numpy as np

data = open('inputs/day9.txt').read().splitlines()

basinList = []
rows = len(data)
cols = len(data[0])
boolList = [[False]*cols for i in range(rows)] #list of bool list with col number of false values

def flowDirections(row, col):      
    b,boolList[row][col] = 1, True #literal, set list to 1 when true 
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #index directions
        rowFlow = row + x #increment through data
        colFlow = col + y  
        if 0 <= rowFlow < rows and 0 <= colFlow < cols and data[rowFlow][colFlow] != '9' and not boolList[rowFlow][colFlow]:  #find basin, exclude height 9
            b += flowDirections(rowFlow, colFlow) # recursive to sum basins 
    return b

for r in range(rows): 
    for c in range(cols):
        if data[r][c] != '9' and not boolList[r][c]:
            basinList.append(flowDirections(r, c)) 

print(np.prod(heapq.nlargest(3, basinList))) #multiply largest 3


