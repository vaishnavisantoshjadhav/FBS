"""Write a program to check if given number is Armstrong number or not.
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
4*4*4*4)"""
num = int(input("Enter the number: "))

temp = num
sum = 0
count = 0

while num > 0:
    count = count + 1
    num = num // 10

num = temp

while num > 0:
    digit = num % 10
    sum = sum + digit ** count
    num = num // 10

if sum == temp:
    print(f"{temp} is an Armstrong Number.")
else:
    print(f"{temp} is not an Armstrong Number.")