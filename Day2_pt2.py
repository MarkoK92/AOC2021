
import pandas as p
f,d,a = 0,0,0
data = p.read_csv("inputs/day2.txt", header=None, sep=' ')

for r, row in data.iterrows(): 
    if(row[0] == 'forward'): 
        f += int(row[1]) 
        d += int(row[1]) * a     
    elif(row[0] == 'down'): 
        a += int(row[1]) 
    else: a -= int(row[1])

print(f * d)