#wap wich reads list of int and return a new list bt eliminating the duplicate
#elements in the list

a=[1,2,5,2,4,1,3,6,6,6]
b=[]
for i in a:
    for j in a:
        if(i!=j and i not in b):
            b.append(i)
print(b)
