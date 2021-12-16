with open('inputs/day16.txt') as data:
    bitCollection = list(bin(int(data.read().strip(), 16))[2:] # first base 16 to int, then to binary from second index
    .zfill(len(data.read().strip()) * 4)) # bit shift left for the lenth 4 times

ver = 0

def PacketLooper(data):
    ev, p = ToHexDeciaml(data[:3]), data[3:] # take last 4 for endVersion and first 4 for paket
    global ver #use global version
    ver += ev #increase version
    subValue, p = ToHexDeciaml(p[:3]), p[3:] # take last 4 for subValue and first 4 for paket
    if subValue == 4: # check for th index
        listValues = []
        while True:
            n, p = p[:5], p[5:] #take last 4 for group and first 4 for p
            listValues += n[1:] 
            if n[0] == '0': break # found bits
        return ToHexDeciaml(listValues), p

    subValueLen = p.pop(0)
    subValues = []
    if subValueLen == '0': # check 0
        l, p = ToHexDeciaml(p[:15]), p[15:] #take last 15 for length and first 11 for paket
        sp, p = p[:l], p[l:]
        while sp:
            values, sp = PacketLooper(sp) # recursive store to subValues 
            subValues.append(values)
    else:
        num, p = ToHexDeciaml(p[:11]), p[11:] #take last 11 for num and first 11 for paket
        for i in range(num):
            values, p = PacketLooper(p) # recursive store to subValues 
            subValues.append(values)
    if   subValue == 0: val = sum(subValues) # sum of the values of their sub-packets
    elif subValue == 1: val = product(subValues) 
    elif subValue == 2: val = min(subValues) # minimum of the values of their sub-packets
    elif subValue == 3: val = max(subValues) # maximum of the values of their sub-packets
    elif subValue == 5: val = subValues[0] > subValues[1] #value is 1 if the value of the first sub-packet is GREATER than the value of the second sub-packet, otherwise, their value is 0
    elif subValue == 6: val = subValues[0] < subValues[1] #value is 1 if the value of the first sub-packet is LESS than the value of the second sub-packet; otherwise, their value is 0
    elif subValue == 7: val = subValues[0] == subValues[1] #value is 1 if the value of the first sub-packet is EQUAL to the value of the second sub-packet; otherwise, their value is 0
    return val, p # end valu with 

def product(i): # multiply together the values of their sub-packets
    product = 1
    for num in i: product *= num
    return product

def ToHexDeciaml(b): return int(''.join(b), 2)

print(PacketLooper(bitCollection)[0]) # 2
print(ver) # 1