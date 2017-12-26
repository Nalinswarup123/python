a=[1,2,3,4,5]
b=a      #alicing
b[0]=10
print(a)

c=[x for x in a]  #cloning
a[0]=22
print(a,c)

#transpose of a matrix

l=[[1,2],[4,5],[7,8]]
def trans(mat):
    t=[]
    for i in range(len(mat[0])):
        t.append([])
    print(t)

    for i in range(len(t)):
        for j in range(len(mat)):
            t[i].append(mat[j][i])
    return t

print(trans(l))
