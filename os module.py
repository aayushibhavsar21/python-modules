
import os
import random
print(os.getcwd())

if not os.path.exists("data"):
    os.mkdir("data")

def file_name():
    str=""
    for i in range(3):
        num=random.randint(97,122)
        str=str+chr(num)
    return str

for i in range(7):
    file=file_name()
    file_path=os.path.join("data",file + ".png")

    with open(file_path, 'w'):
        pass



import os
file_list=os.listdir("data")

i=0
for old_name in file_list:
    if old_name.endswith(".png"):
        i+=1
        new_name=f"file{i}.png"
    
        old_path=os.path.join("data",old_name)
        new_path=os.path.join("data",new_name)
        
        os.rename(old_path,new_path)

