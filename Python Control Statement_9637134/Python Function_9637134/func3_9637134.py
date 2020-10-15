def func3 (m, n=5):
   sum1=int(m)+int(n)
   return sum1

s1=func3(30, 20)
print(s1)
#output:50 The program start execution from the function call so the value passed in function parameter get update by the parameters passed while calling function

s1=func3(30)
print(s1)
#output:35 The program start execution from the function call so the value passed in function parameter get update by the parameters passed while calling function

s1=func3(5, 0)
print(s1)
#output:5 The program start execution from the function call so the value passed in function parameter get update by the parameters passed while calling function

s1=func3()
print(s1)
#func3() missing 1 required positional argument: 'm'