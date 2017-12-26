def comb(n,r):
    N=1
    R=1
    p=n-r
    for i in range(1,n+1):
        N=N*i
    for i in range(1,r+1):
        R=R*i
    for i in range(1,p):
        p=p*i
    print('permutation=',N//(R*p))
    print('combination=',N//R)
comb(5,3)
