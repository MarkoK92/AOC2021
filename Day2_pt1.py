import pandas as p

data = p.read_csv("inputs/day2.txt", header=None, sep=' ')

f = data[data[0] == 'forward'][1].astype(int).sum() 
d = data[data[0] == 'down'][1].astype(int).sum()
u = data[data[0] == 'up'][1].astype(int).sum()

print (f * (d - u))