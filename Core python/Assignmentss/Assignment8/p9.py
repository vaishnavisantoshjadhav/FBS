#Write a program to find sum of digits of a number.
def sumofdigit():
    num = int(input('Enter the number:'))
    sum = 0
    while num > 0:
        d = num % 10
        sum = sum + d
        num = num // 10
    print('Sum of digit:',sum)
sumofdigit()
