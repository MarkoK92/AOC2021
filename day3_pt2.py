import sys

data = open('inputs/day3.txt').read().splitlines()

def ls(k):
        nms, bit = data[:], 0
        while len(nms) > 1:            
            s1 = [n for n in nms 
            if n[bit] == '0']

            s2 = [n for n in nms 
            if n[bit] == '1']

            nms = k(s1, s2)
            bit += 1

        return int(nms[0], 2)

#oxygen
oxy = ls(lambda s, s2: s2 
if len(s2) >= len(s) 
else s
)

#scrubber 
sc = ls(lambda s, s2: s 
if len(s2) >= len(s) 
else s2
)

print (oxy * sc)

