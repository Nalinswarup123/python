l=[1,2,3,4,5,6]
f,e=0,len(l)-1
x=int(input('enter element to search'))
for i in range(len(l)):
    m=(f+e)//2
    if(l[m]>x):
        e=m-1
    elif(l[m]<x):
        f=m+1
    elif(l[m]==x):
        print('found at',m+1)
        break
else:
    print('not found')
