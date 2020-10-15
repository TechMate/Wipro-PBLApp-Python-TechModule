import sys
A_ADID = int(sys.argv[1])
B_ADID = int(sys.argv[2])
con1 = input("Enter the opertion")
if(con1 =="add"):
    p = A_ADID + B_ADID
    print(p)
elif(con1 =="sub"):
    p = A_ADID - B_ADID
    print(p)
elif(con1 =="mul"):
    p = A_ADID * B_ADID
    print(p)
elif(con1 =="div"):
    p = A_ADID / B_ADID
    print(p)
else:
    print("Enter proper input conditon")
