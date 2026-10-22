"""Write a program to prompt user to enter userid and password. If Id and
password is incorrect give him chance to re-enter the credentials. Let him try 3
times. After that program to terminate."""

correct_user_id = 'admin'
correct_password = "1234"

for i in range (3):
    user_id = input('enter userid:')
    password = input('Enter password:')

    if user_id == correct_user_id  and password == correct_password :
        print('Login successfully')
        break
    else:
        print("Invalid userid and pass")
else:
    print("3 attempted completed program terminated")        