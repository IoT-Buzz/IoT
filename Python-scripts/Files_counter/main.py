import os #import os

count = 0 #default count

d = "." #path of directory 

"""
Main loop to count files 
"""
for path in os.listdir(d): 
    if os.path.isfile(os.path.join(d, path)):
        count += 1
        
print(count)