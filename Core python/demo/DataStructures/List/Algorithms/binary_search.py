def binarySearch(li,serach_ele):
    beg = 0
    end = len(li) - 1
    while(beg <= end):
        print('beg:',beg)
        print('end:',end)
        mid =(beg + end) // 2
        print('mid:',mid)
        if(serach_ele == li[mid]):
            return mid
        elif(serach_ele < li[mid]):
            end = mid -1 
        elif(serach_ele > li[mid]):
            beg = mid + 1 
    else:
        return -1

li = [10,20,30,40,50,60] 
ele =int(input('Enter the elements to find:'))
res = binarySearch(li, ele)
if(res != -1):
    print(f'{ele} is present at the index{res}.')
else:
    print(f'{ele} is not present in list.')               