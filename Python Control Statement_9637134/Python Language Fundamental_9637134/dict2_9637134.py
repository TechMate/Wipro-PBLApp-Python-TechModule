dict1_ADID = {"Bangalore" : 1,  "Chennai" : 2,  "Kochi" : 3}
print(dict1_ADID)

dict1_ADID.update({"Hyderbad":4})
print(dict1_ADID)

del dict1_ADID["Kochi"]
print(dict1_ADID)

dict1_ADID.clear()
print(dict1_ADID)