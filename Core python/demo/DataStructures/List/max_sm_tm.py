li = [45,60,23,50,90,31,100]


max = li[0]
smax = 0

for ind in range(1,len(li)):
    if (li[ind] > max):
        smax = max
        max = li[ind]
    elif(li[ind] > smax):
        smax = li[ind]
print('Max:',max)
print('Smax: ', smax)            