from collections import defaultdict

routes = defaultdict(list)
start = [['start']]
pathList = []

for data in open('inputs/day12.txt'):
	row, col = data.strip().split('-')
	routes[row].append(col)
	routes[col].append(row)

while start:
	direction = start.pop(0) #without last
     
	for cavePath in routes[direction[-1]]: #check if end last
		if cavePath == 'end':
			pathList.append(1) #new path
		elif not cavePath.islower() or cavePath not in direction: #small cave only once
			start.append(direction + [cavePath])

print(sum(pathList))