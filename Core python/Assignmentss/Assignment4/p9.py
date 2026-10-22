#WAP to print all numbers in a range divisible by a given number.

d = int(input('Enter the number:'))
n = int(input('Enter the range:'))

for i in range(1,n+1):
    if(i % d == 0):
        print(i)