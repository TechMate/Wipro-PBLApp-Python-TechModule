fd1=open("in1_ADID", "r")
print(fd1.name) #prints the file name which is in1_ADID
print(fd1.closed) #false because the file is open and it is not closed
print(fd1.mode)# r beacause the file is open in read mode
fd1.close()
print(fd1.closed)# true because the file is closed