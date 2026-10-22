#WAP to check if a given number is prime number or not.
n = int(input('Enter number:'))

for i in range(2,n):   
    if (n % i == 0):
        print(f'{n}number is not prime')
        break
else:
        print(f'{n}number is  prime')
