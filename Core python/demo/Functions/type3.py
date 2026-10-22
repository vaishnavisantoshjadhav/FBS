#return frame will excute then it come outside the function 
#Type 3:

def addition():
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2:'))

    
    sum = num1 + num2
    return sum

res = addition()
print('Result:',res)
