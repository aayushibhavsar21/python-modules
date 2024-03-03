import time 

#time.time() returns a number of seconds since epoch ( the point in time when the time module was initialized ( 1 jan,1970 ) )
t1=time.time()

for i in range(200):
    print(i)

print("execution time of for loop : ",time.time()-t1)




#The time.sleep() function suspends the execution of the current thread for a specified number of seconds

print("start:",time.time())
time.sleep(2)
print("end:",time.time())




#The time.strftime() function formats a time value as a string, based on a specified format.

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)