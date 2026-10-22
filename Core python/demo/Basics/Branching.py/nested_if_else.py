#the next condition depends on T/F of previous condition

gender = input('Enter gender(F/M):')
age = int(input('Enter age:'))

if(gender == 'M'):
    if(age >= 21):
        print('boy eligible for marraige.')
    else:
        print('boy not eleigible.')
else:
    if(age >= 18 ):
        print('girl eligible for marraige.')
    else:
        print('girl not eligible.')    
