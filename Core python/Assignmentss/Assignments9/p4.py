#Write a program to find sum of n numbers using recursion.

def sumofnum(num):
    if num == 0:
        return 0
    else:
        return num + sumofnum(num-1)
num = int(input('Enter the number:'))
print('Sum',sumofnum(num))    


