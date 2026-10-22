##recursive function direct 
def fun(n):
    print("Function executing...")
    if(n>1):
            fun(n - 1)
n = 5
fun(n)