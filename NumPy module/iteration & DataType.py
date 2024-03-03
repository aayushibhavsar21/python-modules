import numpy as np 

arr = np.array( [1,2,3,4,5] )
print(arr.dtype)
arr = np.array( [1,2,3,4,5] ,dtype=np.float32 )         # method 1 to change data type
print(arr , arr.dtype)

arr = np.array( [5.1,7.2,4.3,4.8,5.1] )
print(arr.dtype)
new = np.int32(arr)                                     # method 2 to change data type
print(new , new.dtype )

arr = np.array(['1','2','3','4','5'])
print(arr.dtype)
arr = np.array( ['1','2','3','4','5'] , dtype="U11" )   # method 3 to change data type
print(arr , arr.dtype)
arr = np.array(['a','b','c','d','e',1,2,3])
print(arr.dtype)
new=arr.astype("U1")                                    # method 4 to change data type
print(new , new.dtype)

#____iteration____
for i in arr:
    print(i)

two_d = np.array([[7,8,9],[5,4,3]])

for i in two_d:
    print(i)

for i in two_d:
    for j in i:
        print(j)

for i,d in np.ndenumerate(two_d):
    print(i,d)