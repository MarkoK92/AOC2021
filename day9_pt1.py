
data = open('inputs/day9.txt').read().splitlines()

points = []
rows = len(data)
cols = len(data[0])

def calculate_pts(row,col,rows,cols):
    pts = min(data[row + rind][col + cind] ##increment through data
             for rind, cind in [(-1, 0), (1, 0), (0, -1), (0, 1)] #index directions
             if 0 <= row + rind < rows 
             and 0 <= col + cind < cols)
    return pts 

for row in range(rows):
    for col in range(cols):
        if data[row][col] < calculate_pts(row,col,rows,cols): #recursive to sum pts
            points.append(int(data[row][col]) + 1)

print(sum(points))