#Write a program to print prime numbers between 1 to 100.
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)


for num in range(2, 101):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)