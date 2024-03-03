import numpy as np

#comparison b/w array and list:

list = [j**4 for j in range(1,8)]      
# can store any data type at a time , single dimension , use more memory
print(list)

array1 = np.arange(1,8)**4  #arange ( starting ( by default 0 ) , ending ) 
# can store only 1 data type at a time , can perform any matrix operations , multi dimension ,use less memory
print(array1)



ele=input("enter ele:")
member=[int(i) for i in ele.split()]
array2 = np.array(member)
print(array2)


#____multi dimension array____
ONE_D = np.array([1,2,3])
TWO_D = np.array([[1,2,3],[4,5,6]])
 # np.array([[1,2,3],[4,5]]) - not allowed , both list should have same number of ele
THREE_D = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

print(f"{ONE_D} {ONE_D.ndim} \n {TWO_D} {TWO_D.ndim} \n {THREE_D} {THREE_D.ndim}")

N_D = np.array([1,2,3,4],ndmin=10)
print(N_D)
print(N_D.ndim)
print(np.array([[1],[2],[3]]))



#____zero array____
print(np.arange(5)*0)

print(np.zeros(4))
print(np.zeros((4,3)))  # 4 by 3 array



#____ones array____
ele=[i%(i-1) for i in range(3,8)]
print(np.array(ele))
print(np.ones(5))

print(np.empty(4)) # empty array , it filled array with garbage values



#____diagonal____ 
print(np.eye(3))   # 3 by 3 array
print(np.eye(3,5))   # 3 by 5 array



#____ele with particular gap____ 
print(np.linspace(0,20,num=5))
print(np.linspace(0,20,num=4))
print(np.linspace(1,10,num=4))



#____array with random number____

print(np.random.rand(5))    # rand()-print random value from 0 to 1
print(np.random.rand(2,5))  # 2 by 5 array

print(np.random.randn(5))    # randn()-print random num close to 0. (num can be -ve or +ve)

print(np.random.ranf(5))     # ranf()-print random num floats in [ 0.0 , 1.0) : 0<=val<1  

print(np.random.randint(4,9,10))     # ranf(min , max , no. of ele)-print random num b/w given range
print(np.random.randint(7,24,5))



#____copy and view____
import numpy as np
arr = np.array([1,2,3,4])
copy = arr.copy()  # copy has its own data , change made in original data does not change it
view = arr.view()  # view does not have its own data , change made in original data make changes in it ,too.
arr[2] = 8
print(copy , view)