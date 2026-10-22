
def armstrong():
    num = int(input("Enter a number: "))
    temp = num
    total = 0
    power = len(str(num))

    while num > 0:
        d = num % 10
        total = total + d ** power
        num = num // 10

    if temp == total:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

armstrong()
#For 153, there are 3 digits: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 therefore, 153 is an Armstrong number. ✅
