def selectionSort(li):
    size = len(li)
    for i  in range(0,size - 1):
        mid_ind = i
        for j in range(i+1, size):
            if  (li[j]<li[min_ind]):
                
                mid_ind = j
            li[i],li[mid_ind] =  li[mid_ind], li[i]
li = [60,50,40,30,20,10]
print('Before Sorting:',li)
selectionSort(li)               
print('After Sorting:',li)