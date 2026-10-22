#Write a program to find maximum and minimum element in a list
lst = [10, 20, 5, 40, 15]

max = lst[0]
min = lst[0]

for i in lst:
    if i > max:
        max = i
    if i < min:
        min = i

print('Maximum =', max)
print('Minimum =', min)

