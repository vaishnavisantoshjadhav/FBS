"""Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)"""

import random
id =input('Enter the userid:')
password=input('Enter the password:')

if id =='reva' and password=='1234':
    print('Userid and password are corect')
else:
    print('wrong')


num = random.randint(1000,9999)
print(num)
num1 = int(input('Enter the number2:')) 

if num == num1:
    print('successs')
else:
    print('failed')   