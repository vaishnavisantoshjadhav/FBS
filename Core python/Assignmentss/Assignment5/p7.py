#Write a program to solve the following series :
#1.Find the sum of the series: 1! + 2! + 3! + 4! + ..... + n!

n = int(input('Enter the value of n:'))
sum = 0
fact = 1

for i in range(1,n+1):
    fact = fact * i
    sum = sum + fact

print(' Sum of Series:',sum)    
