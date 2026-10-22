l1=[1,2,3,4,56,66,12]
l2=[10,22,3,4,56,66,50]
l3=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
print(l3)