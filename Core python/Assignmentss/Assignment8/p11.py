#Write a program to check if entered number is a palindrome or not.

def palindrome():
    num = int(input('Enter the number:'))
    temp = num
    rev = 0

    while num > 0:
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
    if temp == rev:
        print('number is Palindrome')
    else:
        print('Number is not palindrome')
palindrome()    
