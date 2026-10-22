#12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter 3 digit number:'))
first = num // 100
last = num % 10

if first == last:
    print("Palindrome")
else:
    print("Not Palindrome")