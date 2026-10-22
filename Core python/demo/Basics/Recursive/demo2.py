#indirect recursive function example

def sumofSeries(n):
    if(n <= 0):
        return 0
    else:
        return n + sumofSeries(n - 1)
n = 5
res = sumofSeries
print(res)