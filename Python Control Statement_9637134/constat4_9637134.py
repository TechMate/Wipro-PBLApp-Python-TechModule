import os

a = os.getcwd()
print(a)

b = os.environ['HOME']
print(b)


if(a == b):
    print("Both the directories are same")
else:
    print("Both the directories are diffrent")
