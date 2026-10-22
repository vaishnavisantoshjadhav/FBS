#Write a program to print Fibonacci series using recursion.
def fibo(num):
    if num==1 or num==2:
        return 1
    else:
        return fibo(num - 1)+ fibo(num - 2)
num = int(input('Enter the number:'))
print('Fibonacci series:',fibo(num))    