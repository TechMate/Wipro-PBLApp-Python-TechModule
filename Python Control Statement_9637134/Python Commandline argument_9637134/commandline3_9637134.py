import sys
cmd_arg = (sys.argv)
print(cmd_arg)


print("The 1st argument :",cmd_arg[1],"The 2nd argument : ",cmd_arg[3])

print("The 0th argument :",cmd_arg[0])

length = len(cmd_arg)
print("Number of commandline argument passed: ",length)

cmd_arg.pop(0) #The elements passed by command line are stored in form of string in a list,So i have use the pop fuction to remove the asgv[0] element which will be the file name,
               #so that i can convert the list elements type(string) to int to perform arthimetic operation

for i in range(0,len(cmd_arg)): #here is the converstion of list elements from string to int type
    cmd_arg[i] = int(cmd_arg[i])
total = sum(cmd_arg)
avg = total / len(cmd_arg)
print("The average is",avg)
