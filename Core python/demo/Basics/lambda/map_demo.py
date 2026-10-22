#to find square of no

#def sq(n):
#    return n * n
data = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]

#method 1
#res = list(map(sq,data))

#method 2

res = list(map(lambda n: n * n,data))
print(res)