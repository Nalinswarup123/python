def fib(n):
    fibtable=[0,1]
    for i in range(2,n):
        fibtable.append(fibtable[i-1]+fibtable[i-2])
    return(fibtable)
print(fib(0))



def fact(n):
    fac=1
    if n==0:
        return fac
    else:
        for i in range(1,n+1):
            fac=fac*i
        return(fac)
print(fact(6))
