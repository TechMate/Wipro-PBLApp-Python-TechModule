try:
    dict3_ADID = {'k1':10, 'k2':20, 'k3':30}
    print(dict3_ADID['k5'])
except KeyError:
    print("KeyError: 'k5', the key is not present in dict3_ADID")
finally:
    print("always executes")

