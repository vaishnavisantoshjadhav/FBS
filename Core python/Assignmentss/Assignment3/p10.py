"""Write a program to check if person is eligible to marry or not (male age >=21 and
female age>=18)"""


age = int(input('Enter your age:'))
gender = input('Enter the gender:')

if gender == 'male' and age >= 21 :
    print('ELIGIBLE to marry')
elif gender == 'female' and age >= 18 :
    print('NOT Eligible to marry')
else:
    print('Gap ghari basss mg')