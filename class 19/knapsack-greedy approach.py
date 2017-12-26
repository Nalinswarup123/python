capacity=float(input("enter the capacity"))
capacityRemaining=capacity
n=int(input("Enter no of items"))
items=[]
weight=[]
price=[]
ratio=[]
for i in range(n):
    items.append(input("Enter item name"))
    weight.append(float(input("enter item name weight")))
    price.append(float(input("Enter item price")))
    ratio.append(price[i]/weight[i])
choice=int(input("Enter 1 for minimizing weight \n 2 for maximizing price \n 3 for maximizing density"))
count=0
weightOfBag=0
totalsum=0
while count<n:
    if choice==1:
        mweight=min(weight)
        pos=weight.index(mweight)
    elif choice==2:
        mprice=max(price)
        pos=price.index(mprice)
        mweight=weight[pos]
    else:
        mratio=max(ratio)
        pos=ratio.index(mratio)
        mweight=weight[pos]
    if mweight<=capacityRemaining:
        print(items[pos],"inserted into bag")
        totalsum=totalsum+price[pos]
        weightOfBag=weightOfBag+mweight
        capacityRemaining=capacity-weightOfBag
    del items[pos]
    del weight[pos]
    del price[pos]
    del ratio[pos]
    count=count+1
    if capacity==weightOfBag:
        break
print("total price in bag:",totalsum,"\ntotal weight of bag:",weightOfBag)

