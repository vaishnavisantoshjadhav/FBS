#Calculate total salary based on Basic, DA = 10%, TA = 12%, HRA = 15%
basic = float(input("Enter basic salary: "))

da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100

total_salary = basic + da + ta + hra

print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary =", total_salary)