#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

math = int(input('Enter the Math marks:'))
eng = int(input('Enter the eng marks:'))
mar = int(input('Enter the marathi marks:'))
sci = int(input('Enter the science marks:'))
geo = int(input('Enter the geography:'))

grade = math + eng + mar + sci + geo

percentage = grade / 5
if percentage >= 90:
    print('First class')
elif percentage >= 80:
    print('Second class')
elif percentage >= 35:
    print('third class')
else:
    print('failed')
print(percentage)