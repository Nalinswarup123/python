
a=[[1,2,3],[3,4,5]]
b=[[1,2],[3,4],[5,6]]
#c=[[]for i in range(len(a))]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(b)):
            c[i][j]=(c[i][j]+a[i][k]*b[k][j])
print(c)
