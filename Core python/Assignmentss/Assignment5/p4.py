#WAP to print Armstrong number within a given range

start = int(input("Enter staryting number:"))
end = int(input("Enter end number:"))

for i in range(start,end+1):
    n=i
    sum=0

    while n > 0: 
        digit= n % 10
        sum = sum + digit**3

        n = n // 10
    if sum == i:
        print(i)    