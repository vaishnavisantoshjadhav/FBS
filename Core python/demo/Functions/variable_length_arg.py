#variable  length argument
#1.to pass multiple parameter tor function
#mention 1 asterisk * =
#

def add(*data):
    sum = 0
    for val in data:
        sum += val
    return sum

res = add(20,23,50,6,7,1,2)
print(res)
    