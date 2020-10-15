import getpass
user = input("Enter the user name")
validusn = getpass.getuser()
print(validusn)
if(user == validusn):
    print("valid user on console")
else:
    print("invalid user on console")