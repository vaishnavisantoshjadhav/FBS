#Write a program to reverse a given number using recursive function.

def reverse(num,rev):
    if num == 0:
        return rev
    else:
        d = num % 10
        rev = rev * 10 + d
        return reverse(num//10,rev)
num = int(input('enter the number:'))
print('Revers number:',reverse(num,0))    