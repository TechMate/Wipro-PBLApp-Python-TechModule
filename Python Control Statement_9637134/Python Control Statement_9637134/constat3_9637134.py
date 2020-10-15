import os
fn = input("Enter the filename")
if os.path.isdir(fn):
    print("its is directory")
elif os.path.isfile(fn):
    print("its is a normal file")
else:
    print("Its is a soft link")