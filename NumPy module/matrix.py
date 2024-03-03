
matrix1 = np.matrix([[1,2],[4,5]])
matrix2 = np.matrix([[6,7],[8,9]])
print(type(matrix1))
print(matrix1*matrix2)
print(matrix1.dot(matrix2))

array1 = np.array([[1,2],[4,5]])
array2 = np.array([[6,7],[8,9]])
print(type(array1))
print(array1*array2)


import numpy as np
matrix1 = np.matrix([[1,2],[3,4]])

print(np.transpose(matrix1))
print(np.swapaxes(matrix1,0,1))
   
print(matrix1**2)  
print(np.linalg.matrix_power(matrix1,3))   
print(np.linalg.matrix_power(matrix1,0))   
print(np.linalg.matrix_power(matrix1,-2)) 
print(np.linalg.det(matrix1)) 
print(np.linalg.inv(matrix1))  

#   [[1,2]  -> ______1_______ [[4 -2]  -> __1__ [[4 -2]   -> [[-2   1 ]
#    [3,4]]    [(1*4)-(2*3)]   [-3 1]]     -2    [-3 1]]      [1.5 0.5]]



