tables = [] 
endTable = []
tablEnum = {}
tableTotal = {}
rows = {}
cols = {}

data = open('inputs/day4.txt').read().splitlines()

bingoNums = list(map(int, data[0].split(',')))
last = [False] * len(bingoNums) #default not set


for sindex in range(2, len(data), 6):
    tables.append([])
    for bindex in range(sindex, sindex + 5):
        row = list(map(int, data[bindex].split()))
        tables[-1].append(row)

for bindex, table in enumerate(tables):
    for rindex, row in enumerate(table):
        for cindex, num in enumerate(row):
            if num not in tablEnum:
                tablEnum[num] = set()
            tablEnum[num].add((bindex, rindex, cindex))
            tableTotal[bindex] = tableTotal.get(bindex, 0) + num
            rows[bindex] = [5] * 5 #every 5th number
            cols[bindex] = [5] * 5

for num in bingoNums: 
    for indexT, indexR, indexC in tablEnum.get(num, []):
        tableTotal[indexT] -= num
        rows[indexT][indexR] -= 1
        cols[indexT][indexC] -= 1
        if not last[indexT] and (rows[indexT][indexR] == 0 
        or cols[indexT][indexC] == 0):
            last[indexT] = True #is correct one
            endTable.append(num * tableTotal[indexT])

print(endTable[0]) #choose specific table part 1
print(endTable[-1]) #finalscore