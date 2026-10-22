#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a1 = int(input('Enter first angel of triangle:'))
a2 = int(input('Enter second angel of triangle:'))
a3 = int(input('Enter 3rd angel of traingle:'))

if a1 == a2 == a3:
    print('Triangle is Equilateral')
elif a1 == a2 or a2 == a3 or a3==a1:
    print('Triangle is isoscales ')
elif a1 != a2 or a2 != a3 or a3 != a1:
    print('Triangle is scalene')    