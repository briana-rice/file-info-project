
import os  

file_info_list = []  
for file in os.listdir():  
    if os.path.isfile(file):  
        file_info_list.append({"name": file, "size": os.path.getsize(file)})  

print(file_info_list)  
