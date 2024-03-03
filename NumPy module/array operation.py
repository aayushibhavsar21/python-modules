import numpy as np

var1 = np.array([1,2,3,4])

print ( f"      {var1+3}     ,        \n{var1-2}       ,        \n{var1*3}       ,       \n{var1/3}      ,      \n{var1%4}    ,     \n{var1**2}      ,      \n{1/var1}        " )
print ( f"\n{np.add(var1,3)} , \n{np.subtract(var1,2)} , \n{np.multiply(var1,3)} , \n{np.divide(var1,3)} , \n{np.mod(var1,4)} , \n{np.power(var1,2)} , \n{np.reciprocal(var1)} , \n{np.sqrt(var1)}" )

print("min:",np.min(var1),"pos:",np.argmin(var1))
print(np.cumsum(var1))  # for result arr = 1st pos as it is , for next positions :n pos of result arr + n+1 pos of main arr 
                        # cumsum is useful to find mean in statistic

var2 = np.array([5,6,7,8])

print ( f"      {var1+var2}     ,        \n{var2-var1}       ,        \n{var1*var2}       ,       \n{var2/var1}      ,     \n{var2%var1}     ,      \n{var2**var1}     " )
print ( f"\n{np.add(var1,var2)} , \n{np.subtract(var2,var1)} , \n{np.multiply(var1,var2)} , \n{np.divide(var2,var1)} , \n{np.mod(var2,var1)} , \n{np.power(var2,var1)} " )

print("max:",np.max(var2),"pos:",np.argmax(var2))
print(np.sin(var2),"\n",np.cos(var2))


two_d1 = np.array([[1,2,3],[4,5,6]])
two_d2 = np.array([[7,8,9],[5,4,3]])

print ( f" \n{ two_d1 + two_d2 } " ) # all arithmetic operations can be performe on 2D array same as we performed it on 1D array 

print( f" min:{np.min(two_d2,axis=0)} ,pos:{np.argmin(two_d2)} \nmax:{np.max(two_d2,axis=1)} , pos:{np.argmax(two_d2)}")
     # axis-0 column(min nums in all cols )                  # axis-1 row ( max nums in all rows )

print(two_d1.shape) 



#____broadcasting method____

arr1 = np.array([[2,3],[5,1]])
arr2 = np.array([[3,6],[7,3]])
print(arr1+arr2)  # both array have same dimension 

# If the arrays do not have the same number of dimensions, then a "1" will be repeatedly added to the smaller array's shape until both shapes have the same length.this is breadcasting
arr1 = np.array([[2],[1]])     #(2,1) -> 1 will add to column so it become [[2 2]
                               #                                            [1 1]]  so now it is compatible with arr2 to perform addition 
arr2 = np.array([[2,7],[1,3]]) #(2,2)
print(arr1+arr2)

arr1=np.array([1,2,3])         #(1,3) -> 1 will add to row 2 times -> (3,3) -> [[1 2 3]
                               #                                                [1 2 3]
                               #                                                [1 2 3]]
arr2=np.array([[1],[2],[3]])   #(3,1) -> 1 will add to column 2 times -> (3,3) -> [[1 1 1]
print(arr1+arr2)               #                                                   [2 2 2]
                               #                                                   [3 3 3]]