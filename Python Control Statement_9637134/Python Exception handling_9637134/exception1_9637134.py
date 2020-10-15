try:
    f = open("newfile1_ADID",'r')
    print(f.read())#FileNotFoundError
except FileNotFoundError:
    print("THe file is not present in working directory")
finally:
    print("finally always executes")
