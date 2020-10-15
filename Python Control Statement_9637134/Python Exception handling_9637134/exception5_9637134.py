try:
    list3_ADID = [10, 20, 30, 40, 50]
    print(list3_ADID[7])
except IndexError:
    print("IndexError: list index out of range")
finally:
    print("Always Exceutes")