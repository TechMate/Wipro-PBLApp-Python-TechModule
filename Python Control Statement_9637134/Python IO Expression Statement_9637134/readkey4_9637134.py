userlist_ADID = []
for i in range(0,5):
    a = input("Enter the user names")
    userlist_ADID.append(a)


stream_ADID = []
for i in range(0,5):
    a = input("Enter the stream names")
    stream_ADID.append(a)


userdict_ADID = {}
for i in userlist_ADID:
    for j in stream_ADID:
        a = i
        b = j
    userdict_ADID[a] = j
print(userdict_ADID)




