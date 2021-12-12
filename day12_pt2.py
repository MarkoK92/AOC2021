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

	for cavePath in routes[direction[-1]]:
		checkSmall = cavePath.islower() and cavePath in direction #check if small and is in direction list
		if cavePath == 'end':
			pathList.append(1) #new path
		elif cavePath != 'start' and not (direction[0] == '*' and checkSmall): #fill direction path that does is not start and is big
			start.append((['*'] if checkSmall else []) + direction + [cavePath]) 

print(sum(pathList))