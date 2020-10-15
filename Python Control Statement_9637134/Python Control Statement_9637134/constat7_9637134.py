import os
a = os.getcwd()
print("The current working directory",a)
d = input("Enter the directory name")
if os.path.isdir(d):
    print("Unable to create new Directory")
else:
    os.mkdir(d)
entries = os.listdir(a)
print("The contents of working directory",entries)
