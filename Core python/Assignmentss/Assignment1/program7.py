import math
a = float(input('Enter value of a : '))
b = float(input('Enter value of b : '))
c = float(input('Enter value of c : '))

D = b**2 - 4*a*c

if D>0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)

    print(root1, root2)
elif D == 0:
    root = -b / (2*a)

    print('both roots are equal = ' ,root)
else:
    print('roots are imaginary')