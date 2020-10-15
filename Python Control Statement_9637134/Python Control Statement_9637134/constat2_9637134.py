import sys
import os 
import pwd 
filename = sys.argv[1]
st = os.stat(filename)
ownername = pwd.getpwuid(st.st_uid).pw_name
print("The owner is:",ownername)
print("File size in bytes is",st.st_size)

