f = open("in1_ADID",'rb')# seek() function negative offset works only when file is opened in binary mode.
print(f.tell())
f.seek(-11,2)
print(f.read().decode('utf-8'))#converting to binary to string

f.seek(-13,1)
print(f.readline().decode('utf-8'))

f.seek(5,0)
print(f.readline())

print(f.tell())

