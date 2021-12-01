data = [*map(int, open('inputs/day1.txt', 'r'))]

d1 =  sum(1 for i in range(1,len(data)) 
            if data[i] > data[i-1])
            
d2 =  sum(1 for i in range(3,len(data)) 
            if data[i] > data[i-3])

print(d1)
print(d2)



