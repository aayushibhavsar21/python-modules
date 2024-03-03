import numpy as np

#____search____
array = np.array([1,2,3,4,2,6,7,2,8])

print(np.where( array == 2 ))
print(np.where( array%2 == 0 ))
print(np.unique( array , return_index=True , return_counts=True ))

new=np.sort(array) 

print(new,np.searchsorted(new,5))  # return index where the specified value would be inserted to maintain order
print(new,np.searchsorted(new,[5,8,9],side="right"))  # set index num 0 from right side


filt = [True,False,True,False,True]
print(array[filt] , type(array[filt]))

np.random.shuffle(array)
print(array)



#____insert/delete____

array = np.array(["a","b","c","d","e"]) 
array = np.insert(array,2,"t") # (var name , pos , value )
array = np.insert(array,(2,4),"v")
array = np.append(array,"q")   # append at the end of the array
print(array)


two_d = np.array([[1,2,3],[4,5,6]])

new1 = np.insert(two_d , 2 , 7 , axis=0)
print(new1)

new2 = np.insert(two_d , 2 , 7 , axis=1)
print(new2)

new = np.insert(two_d , 2 , [7,8,9] , axis=0)
print(new)

two_d = np.append(two_d,[[7,8,9]],axis=0)
print(two_d)

array = np.array([1,2,3,4,2,6,7,2,8])
array = np.delete(array,2)  # delete value at index 2
print(array)