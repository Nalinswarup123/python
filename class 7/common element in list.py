l1=[1,2,5,8,7,4,9,6]
l2=[4,1,8,6,9,7,2,3,11]
l3=[]
def fun():
    for i in l1:
        for j in l2:
            if(i==j):
               l3.append(i)
fun()
print(l3)


#sum of elements of a list
s=0
for i in l1: s=s+i
print(s)


del l1[2:5]
print(l1)

