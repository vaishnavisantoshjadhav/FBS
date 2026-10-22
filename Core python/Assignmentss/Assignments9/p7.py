#Write a program to find sum of digits using recursion.

def sumofdigit(num):
    if num == 0:
        return 0
    else:
        d = num % 10
        return d + sumofdigit(num//10)
num = int(input('Enter the number:'))
print('Sum of digit:',sumofdigit(num))    
    