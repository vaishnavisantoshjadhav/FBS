#Write a program to input angles of a triangle and check whether triangle is valid or not.

a1 = int(input('Enter first angel of triangle:'))
a2 = int(input('Enter second angel of triangle:'))
a3 = int(input('Enter 3rd angel of traingle:'))
sum = a1 + a2 + a3
if sum == 180:
    print('Triangle is Valid')
else:
    print('Triangle is not Valid')    