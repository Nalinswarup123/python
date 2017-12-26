a=[]
n=int(input('enter size'))
a=[0]*n
for i in range(n):
    a[i]=int(input('enter element'))
print(a)

def merge(a,l,m,h):
    print('splitting',a)
    n1=m-l+1
    n2=h-m
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=a[i+l]
    for j in range(n2):
        R[j]=a[m+j+1]
    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        a[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        a[k]=R[j]
        j+=1
        k+=1
    print('merging',a)
        
def mergesort(a,l,h):
    if l<h:
        m=(l+h)//2
        mergesort(a,l,m)
        mergesort(a,m+1,h)
        merge(a,l,m,h)
mergesort(a,0,n-1)
print(a)
