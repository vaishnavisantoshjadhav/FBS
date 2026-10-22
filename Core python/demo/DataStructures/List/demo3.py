li = [1, 6, 5, 7, 3, 2, 9, 11, 36]

count = 1
sum = 0

for var in li:
    if count % 3 == 1:
        sum = sum + var
    count = count + 1

print(sum)