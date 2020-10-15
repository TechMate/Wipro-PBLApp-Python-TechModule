mytuple1_ADID = (1,2,3,4,5,6,7,8,9,10)
for i in mytuple1_ADID:
    print(i)

mytuple1_ADID[1] = 100
for i in mytuple1_ADID:
    print(i)

"""TypeError: 'tuple' object does not support item assignment
The reason is because tuple are immutable"""