#filter lambda fu
#TRUELY  :
#FALSY:0,NONE ,FALSE,BLANK,'',

data = [1,2,3,4,5,6,7,8,9,10]
res = list(filter(lambda n: n * n,data))
print(res)