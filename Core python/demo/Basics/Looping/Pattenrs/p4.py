#for 1 23 456 78910
#1 
#2 3 
#4 5 6 
#7 8 9 10 

#for i in range(1, 5):
#    for j in range(1, i + 1):
#       print(i * (i - 1) // 2 + j, end=" ")
#    print()

k = 1

for i in range(1, 5):
    for j in range(1, i + 1):
        print(k, end=" ")
        k+=1
    print()