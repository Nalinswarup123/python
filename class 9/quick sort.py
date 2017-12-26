def partition(lst,low,high):
    i=low-1
    pivot = lst[high]
    for j in range(low,high):
        if(lst[j]<=pivot):
            i=i+1
            lst[i],lst[j]=lst[j],lst[i]

    lst[i+1],lst[high]=lst[high],lst[i+1]
    return(i+1)
def quicksort(lst,low,high):
    if(low < high):
        pi=partition(lst,low,high)
        quicksort(lst,low,pi-1)
        quicksort(lst,pi+1,high)

a=[5,7,8,6,2,1]
n=len(a)
quicksort(a,0,n-1)
print('sorted list is')
print(a)


                           
