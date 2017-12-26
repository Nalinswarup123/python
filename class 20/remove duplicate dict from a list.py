#wap a program to remove duplicate element from dict stored in list
l=[{'a':1,'b':2},{'a':1,'b':2},{'a':3,'b':4},{'c':3,'d':4}]
k=len(l)
for i in range(0,k-1):
    for j in (i+1,k):
        if(l[i]==l[j]):
            del(l[j])
            k=k-1

print(l)


'''
a=[{'a':1,'b':2},{'a':1,'b':2},{'a':3,'b':4},{'c':3,'d':4}]
for i in range(0,len(a)):
    for k in a[i].keys():
        for j in range(i+1,len(a)):
            if k in a[j]:
                del(a[j][k])

print(a)'''
'''
l=[{'a':1,'b':2},{'a':1,'b':2},{'a':3,'b':4},{'c':3,'d':4}]
del(l[2])
print(len(l))
print(l[2])'''
