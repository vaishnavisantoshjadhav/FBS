#1¹ + 2² + 3³ + ... + nⁿ

#Program:
def sum_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i ** i
    return sum

n = int(input("Enter n: "))
print("Sum of series =", sum_series(n))

