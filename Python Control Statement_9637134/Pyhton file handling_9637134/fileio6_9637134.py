f = open("in1_ADID",'rb')#seek() function negative offset works only when file is opened in binary mode.
print(f.tell())

f.seek(0)
print(f.read(11).decode('utf-8'))#converting to binary to string

f.seek(-11,2)
print(f.read().decode('utf-8'))

print(f.tell())
f.seek(0)
print(f.tell())
