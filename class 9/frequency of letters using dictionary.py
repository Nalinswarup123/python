#wap using dict which count the frequency of all the characters of Mississippi
x={}
for i in 'Mississippi':
    x[i]=x.get(i,0)+1
y=x.items()
print(sorted(y))
