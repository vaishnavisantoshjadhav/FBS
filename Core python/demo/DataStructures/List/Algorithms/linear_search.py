
def linearSearch(li,search_ele):
    for ind in range(0,len(li)):
        if(search_ele == li[ind]):
            return ind
    else:           #we have taken else  outer in for loop because it will check all the list firts and then give o/p
        return -1

li = [56,23,96,78,88,55,34] 
ele =int(input('Enter the alements to find:'))
res = linearSearch(li, ele)
if(res != -1):
    print(f'{ele} is present at the index{res}.')
else:
    print(f'{ele} is not present in list.')       