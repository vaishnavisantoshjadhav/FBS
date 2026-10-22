#Write a program to input all sides of a triangle and check whether triangle is valid or not.

a1 = int(input('Enter first angel of triangle:'))
a2 = int(input('Enter second angel of triangle:'))
a3 = int(input('Enter 3rd angel of traingle:'))
if a1 + a2 > a3  and a2 + a3 > a1 and a3 + a1 > a2:
    print('Triangle is Valid')
else:
    print('Triangle is not valid')