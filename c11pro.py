import os
import shutil
source="C:/Users/master/Desktop"
list_of_files=os.listdir(source)
print(list_of_files)
for i in list_of_files:
    root,ext=os.path.splitext(i)
    print("the root of the image ",root)
    print("the extenction of the image ",ext)


