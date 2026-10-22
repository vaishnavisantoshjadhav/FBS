##d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10


a = int(input("Enter the value of a:"))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print("Sum of series =", sum)

"""For a = 2, the series is:

2¹/1 + 2²/2 + 2³/3 + ..... + 2¹⁰/10

The loop calculates each term and adds it to sum.

Note: The result may contain decimal values because / performs division in Python."""