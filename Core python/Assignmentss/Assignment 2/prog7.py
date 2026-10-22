num = int(input('Enter the number: '))
h = num // 100
t = (num // 10) % 10
u = num % 10

sum = h + t + u

print('sum of three digit no: ',sum)