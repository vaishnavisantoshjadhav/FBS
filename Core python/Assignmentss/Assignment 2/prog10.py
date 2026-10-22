#Reverse a three-digit number
num = int(input("Enter a three-digit number: "))

digit1 = num % 10
num = num // 10

digit2 = num % 10
num = num // 10

digit3 = num % 10

reverse = (digit1 * 100) + (digit2 * 10) + digit3

print("Reverse number =", reverse)