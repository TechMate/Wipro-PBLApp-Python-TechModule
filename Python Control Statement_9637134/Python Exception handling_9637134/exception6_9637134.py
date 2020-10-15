num1_ADID = int(input("Enter the number"))
num2_ADID = int(input("Enter the number"))
try:
    sub1_ADID = num2_ADID - num1_ADID
    if num1_ADID > num2_ADID:
        raise Exception("connot subtract greater number from smaller number")

finally:
    print(sub1_ADID)

"""here substracting 100 from 85 is not a exception error to catch this exception we need to manually raise a exception"""