#x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input('Enter the value of x:'))
n = int(input('Enter the terms:'))

sum = 0
sign = 1


for i in range(1,n+1):
     sum = sum + sign * (x ** i) / (2 * i - 1) 
     sign = sign * -1 
print("Sum of series =", sum)