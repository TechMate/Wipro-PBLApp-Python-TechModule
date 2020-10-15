f = open("newfile1_ADID",'r')#No such file or directory: 'in1_ADI'

f = open("newfile1_ADID",'w')#it will create a new file in working directory by name in1_ADI

s1_ADID = " this is the newline added at end"
f.write(s1_ADID)

f = open("newfile1_ADID",'r')
print(f.read())

f = open("newfile1_ADID",'w')
s1_ADID = " this is the newline added at end"
f.write(s1_ADID)
f = open("newfile1_ADID",'r')
print(f.read())
""" here its has added one more line in newfile1_ADID.txt"""

