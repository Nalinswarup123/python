#counting combination
def ncr(n,r):
    c=[[0]*(r+1) for i in range(n+1)]
    print(c)
    for i in range(n+1):
        for j in range(r+1):
            if j==0:
                c[i][j]=1
            elif i==j:
                c[i][j]=1
            elif i>j:
                c[i][j]=c[i-1][j-1]+c[i-1][j]

    print(c)
    return c[n][r]
print(ncr(5,2))
    
