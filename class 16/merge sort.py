def mergesort(alist):
    print('splitting',alist)
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0

        while(i<len(lefthalf) and j<len(righthalf)):
            if(lefthalf[i]<righthalf[j]):
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while(i<len(lefthalf)):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while(j<len(righthalf)):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print('merging',alist)
alist=[]
x=int(input('enter no of elements'))
for i in range(x):
    c=int(input('enter elements one by one'))
    alist.append(c)
mergesort(alist)
print(alist)
