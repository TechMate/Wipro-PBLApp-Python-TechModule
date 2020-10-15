num1_ADID = int(input("Enter the number"))
num2_ADID = int(input("Enter the number"))
try:
    div1_ADID = num1_ADID / num2_ADID
    if num1_ADID < num2_ADID:
        raise Exception("num1 must be greater than num2")


finally:
    print(div1_ADID)

"""here dividing 100 by 200 is not a exception error to catch this exception we need to manually raise a exception"""