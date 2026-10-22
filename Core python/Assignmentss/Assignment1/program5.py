P = float(input('Enter principal: '))
T = float(input('Enter Time: '))
R = float(input('Enter rate: '))

CI = P * (1 + R / 100)**T-P
print('Compound interest=' , CI)
