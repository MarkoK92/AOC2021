
data = open('inputs/day9.txt').read().splitlines()

points = []

def calculate_pts(row,col,rows,cols):
    pts = min(data[row + ri][col + ci] 
             for ri, ci in [(-1, 0), (1, 0), (0, -1), (0, 1)] 
             if 0 <= row + ri < rows 
             and 0 <= col + ci < cols)
    return pts


def calculate_risk(rows, cols):
    rows, cols = len(data), len(data[0])
    for row in range(rows):
        for col in range(cols):
            if data[row][col] < calculate_pts(row,col,rows,cols):
                points.append(int(data[row][col]) + 1)

calculate_risk(len(data) ,data[0])
print(sum(points))