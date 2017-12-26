n=int(input('enter no of elements to be inserted in list'))
l=[]
for i in range (n):
    l.append(int(input('enter elements')))
print(l)

def partition(l,low,high):
    i=low-1
    for j in range(low,high):
        if(l[j]<=l[high]):
            i+=1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[high]=l[high],l[i+1]
    return i+1

def quicksort(l,low,high):
    if(low<high):
        pi=partition(l,low,high)
        quicksort(l,low,pi-1)
        quicksort(l,pi+1,high)
        
quicksort(l,0,n-1)
print(l)
