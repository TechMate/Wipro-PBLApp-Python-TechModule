def func2 (m=10, n=5):
   sum1=int(m)+int(n)
   return sum1

s1=func2(100, 50)
print(s1)
#output:150 The program start execution from the function call so the value passed in function parameter get update by the parameters passed while calling function

s1=func2(100)
print(s1)
#output:105 The program start execution from the function call so the value passed in function parameter get update by the parameters passed while calling function.

s1=func2(10, 5)
print(s1)
#output:15 The program start execution from the function call so the value passed in function parameter get update by the parameters passed while calling function

s1=func2()
print(s1)
#output:15 The program start execution from the function call so the value passed in function parameter get update by the parameters passed while calling function
