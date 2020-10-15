num1_ADID = int(input("Enter the number"))
try:
    sum1_ADID = num1_ADID + num2_ADID
    print(sum1_ADID)
except NameError:
    print("num2_ADID is not defined")
finally:
    print("always executes")

