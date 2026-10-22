
#fibonacci series
n = int(input('how many fibonacci number you want:'))

a =-1
b =1

for i in range(n):
    c = a + b
    print(c, end = '')
    a = b
    b = c