#calculate simple intrest using lambda function

SI = lambda principal, rate,time: (principal * rate * time) / 100

res = SI(1000,12,5) 
print(res)