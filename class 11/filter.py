from functools import reduce
fib=[0,1,1,2,3,5,8]
result=list(filter(lambda x:x%2==0,fib))
print(result)
r=list(filter(lambda x:x%2,fib))
print(r)

f=reduce(lambda x,y:x+y,fib)
print(f)
