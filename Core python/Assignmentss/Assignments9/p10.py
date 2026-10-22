#Write a program to reverse a number using recursion.
def reverse(num, rev):
    if num == 0:
        return rev
    else:
        d = num % 10
        rev = rev * 10 + d
        return reverse(num // 10, rev)

num = int(input('Enter the number:'))
print('Reverse number =', reverse(num, 0))

