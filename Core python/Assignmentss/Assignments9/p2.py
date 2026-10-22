#Write a program to check if given number is Armstrong or not using recursive function.

def armstrong(num, power):
    if num > 0:
        d = num % 10
        num = num // 10
        return d ** power + armstrong(num, power)
    else:
        return 0

num = 153
org_num = num
power = len(str(num))

sum = armstrong(num, power)

if sum == org_num:
    print(f'{org_num} is Armstrong number')
else:
    print(f'{org_num} is not Armstrong number')

