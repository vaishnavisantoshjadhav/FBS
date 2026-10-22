#Find the sum of the series: N + N² + N³ + N⁴ + ..... + Nᴺ

n = int(input('Enter the n number:'))

sum = 0

for i in range(1,n+1):
    sum = sum + n ** i
print('Sum of series :',sum)    
##  For n = 3:

#3¹ + 3² + 3³ = 3 + 9 + 27 = 39