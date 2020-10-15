f = open("in1_ADID","r")
print(f.read(11))
print(f.readline())
"""#output: ning file input output operation in Python
here it has not entirely printed the first line it has skiped 11 character while printing. These occured because 
the read function have already printed those 11 charcaters on console. 
"""