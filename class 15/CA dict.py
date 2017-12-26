d={}
d[(1,2,3)]=4
d[(3,1,2)]=5
d[(4,3)]=1
c=0
for i in d:
    c+=d[i]
print(c)
print(d)
