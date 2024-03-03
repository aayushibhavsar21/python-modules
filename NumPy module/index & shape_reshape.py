import numpy as np

a = np.array([1,2,3] , ndmin=4)
print(a,a.shape)     # no. of rows , columns # [[[[1 2 3]]]] (1, 1, 1, 3) - 1st , 2nd ,3rd list has 1,1,1 list in it and total 3 coloums 
print(a.reshape(-1)) # reshape to one dimension

ar = np.array([1,2,3,4,5,6])
print(ar.ndim)
new_ar=ar.reshape(3,2)   # we can not reshape this array to 3 by 3 bcz for that we do not have enough ele
print(new_ar,new_ar.ndim) 

ar2=np.array([1,2,3,4,5,6,7,8])
print(ar2.reshape(2,2,2))  # 1st list will have 2 lists in it , those 2 lists will have another 2 lists , and array will have 2 columns

#____index & slicing____ 

ar2 = np.array([1,2,3,4,5,6,7,8])
print(ar2[4] , ar2[-3])
print(ar2[1:5] , ar2[1:6:2])  # [start:stop:end] -> array slicing
print(ar2[2:] , ar2[:4])

TwoD = np.array([[1,2,3,7],[4,5,6,8]])
ThreeD = np.array([[[1,2],[4,5]],[[6,7],[8,9]]])

print(TwoD[0,2] , ThreeD[1,1,0])
print(TwoD[1,1:3] , ThreeD[1,0,:2])
   
#                                   0 1                0 0 1
#      (1d)                 (2d)    | |         (3d)   | | |
#    array =[1,2,3,4,5]     array=[[1 2] --0    array=[{[1,2] --0
#    index : 0 1 2 3 4             [3 4]]--1            [3,4]}--1
#                                                       
#                                                   1--{[5,6]  --0
#                                                       [7,8]}]--1
#                                                        | |
#                                                        0 1
    
