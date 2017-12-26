l=[2,9,5,4,8,1,6]
for i in range(len(l)-1):
    m=i
    for j in range(i+1,len(l)):
        if(l[m]>l[j]):
           m=j
    t=l[i]
    l[i]=l[m]
    l[m]=t
print(l)
