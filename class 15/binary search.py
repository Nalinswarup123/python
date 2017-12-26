l=input('enter elements')
print(l)
l=list(map(int,l.split()))
print(l)
n=int(input('enter element to be found'))
s=0
lt=len(l)-1
for i in l:
    m=(s+lt)//2
    if(l[m]<n):
        s=m+1
    elif(l[m]>n):
        lt=m-1
    elif(l[m]==n):
        print('element found ',l[m],' at ',m+1)
        break
else:
    print('element not found')
    
        

