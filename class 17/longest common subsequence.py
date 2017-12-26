#wap to find longest common subsequence from a given string
def lcw():
    u='secret'
    v='bisecti'
    lcw=[[0]*(len(v)+1) for x in range(len(u)+1)]
    print(lcw)
    maxl=0
    for r in range(len(u)-1,-1,-1):
        for c in range(len(v)-1,-1,-1):        
            if u[r]==v[c]:
                lcw[r][c]=lcw[r+1][c+1]+1
            if lcw[r][c]>maxl:
                maxl=lcw[r][c]
    return (maxl)
print(lcw())
