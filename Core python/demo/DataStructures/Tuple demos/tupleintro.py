#1.()
tu = (10,20,20,30,3.14,'abc')
#tu = (10,)
#tu = 10 , 20 ,30,40

#2.Hetrogenous
#print(type(tu))


#3.Ordered
#tuple follows the orfder

#4.Imutable

#tu[0] = 50  # tuple object does not support items assignment
#print(type(tu))
#print(tu)

#5.Duplication allowed
print(type(tu))
print(tu)

#6.Tuple is faster than list
tu = ()
li = []
import sys
print(sys.getsizeof(tu))
print(sys.getsizeof(li))
#in this scenerio tuple is faster than list because sie of tuple is < size of list