mytuple2_ADID = ("apple","mango","banana","orange","lime")
for i in mytuple2_ADID:
    print(i)

print(mytuple2_ADID[0])

mytuple2_ADID[1] = 100
for i in mytuple2_ADID:
    print(i)

"""TypeError: 'tuple' object does not support item assignment
The reason is because tuple are immutable"""