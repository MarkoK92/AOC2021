
data = open('inputs/day11.txt').read().splitlines()

en = [list(map(int, d)) for d in data]

flashPatterns = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] #(x , y) point combinations

def firstFlash(en):
    ff = 100 #start after 100
    while(sum(map(sum, en))) > 0:
        flashingCalc(en)
        ff += 1
    return ff

def flashingCalc(en):
    flash, flashList = 0, []
    for row in range(10): #first 10
        for col in range(10):
            en[row][col] += 1 #increase flash by 1
            if en[row][col] > 9: #if more than 9 increase all by 1
                flash += 1
                en[row][col] = 0 #set to 0 if flashed
                flashList.append((row,col))
    while flashList:
        row, col = flashList.pop()
        for x, y in flashPatterns:
            numRow = row + x 
            numCol = col + y 
            if 0 <= numRow < 10 and 0 <= numCol < 10 and en[numRow][numCol] > 0:
                en[numRow][numCol] += 1 #increase flash by 1
                if en[numRow][numCol] > 9: #if more than 9 increase all by 1
                    flash += 1
                    en[numRow][numCol] = 0 #set to 0 if flashed
                    flashList.append((numRow, numCol)) 
    return flash

print(sum(flashingCalc(en) for i in range(100))) #first 100
print(firstFlash(en))
