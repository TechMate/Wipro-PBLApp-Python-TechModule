f = open("in1_ADID",'r')
list1_ADID = f.readlines()
print(list1_ADID)
print(len(list1_ADID))
f.close()
print(f.read())#output: I/O operation on closed file,
#here the file is closed and it is not possible to read the file without opening the file again.


