
#____join array____

array1=np.array([1,2,3,4])
array2=np.array([7,6,5,4])

print(np.concatenate((array1,array2)))

print(np.stack((array1,array2) , axis=1))
print(np.stack((array1,array2) , axis=0)) 

print(np.hstack((array1,array2)))  # h - join with row 
print(np.vstack((array1,array2)))  # v - join with column 
print(np.dstack((array1,array2)))  # d - join with height 


arr1=np.array([[1,2],[3,4]])
arr2=np.array([[7,6],[5, 4]])

print(np.concatenate((arr1,arr2) , axis=1))
print(np.concatenate((arr1,arr2) , axis=0))

#____split____

array1=np.array([1,2,3,4])
print(np.array_split(array1,3))
print(np.array_split(array1,3)[0])

import numpy as np
arr1=np.array([[1,2],[3,4]])
print(np.array_split(arr1,2,axis=1))
print(np.array_split(arr1,2,axis=0))