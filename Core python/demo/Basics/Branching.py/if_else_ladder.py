#imp   :If previous condition is false then only else condition will execute

num = int(input('Enter number:'))

if(num == 0):
    print('number is Neutral')
elif(num > 0):
    print('Positive')
else:
    print('Negative')    