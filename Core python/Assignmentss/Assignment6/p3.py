###This pattern is called Pascal's Triangle. Each row starts and ends with 1.
for i in range(1, 5):
    num = 1
    for j in range(1, i + 1):
        print(num, end=" ")
        num = num * (i - j) // j
    print()