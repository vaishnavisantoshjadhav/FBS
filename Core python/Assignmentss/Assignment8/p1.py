#Write a program to calculate area of rectangle

def area(length,breadth):
     area = length * breadth
     return area
l = int(input('Enter length:'))
b = int(input('Enter breadth:'))

result =  area(l,b)
print('Area of Rectangle:',result)
    