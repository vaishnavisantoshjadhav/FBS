
#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n

def SumofSeries(n):
    if (n <= 0):
        return 0
    else:
        return n + SumofSeries(n -  1)
n = 8
res = SumofSeries(n)
print(res)