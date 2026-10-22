#for decermenting by one  example *
#                                 * *
#for i in range(1,6):
#   for j in range(1,7-i):
#       print('*', end=' ')
#     print()


#for i in range(1,6):
#    for j in range(i-1,5):
#       print('*', end=' ')
#    print()

#for decrementing no like 5,4,3,2,1
#                         4 3 2 1
for i in range(1,6):
    for j in range(6-i,0,-1):
        print(j, end=' ')
    print()