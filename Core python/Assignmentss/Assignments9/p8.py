#Write a program to check whether a number is prime or not using recursion.
def prime(num,i):
    if num <= 1:
        return False
    if i == 1:
        return True
    if num % i == 0:
        return False
    else:
        return prime(num,i-1)
num = int(input('Enter the number:'))
if prime(num,num-1):
    print(f'{num}number is prime ')
else:
    print(f'{num}number is not prime')    
