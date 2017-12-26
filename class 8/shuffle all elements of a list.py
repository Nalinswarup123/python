#wap to shuffle all the elements stored in a 2D list(using random)
from random import*
a=[[1,2,3],[4,5,6],[7,8,9]]
l=[[],[],[]]
#we can shuffle the elments in 1D list using random.shuffle but if we shuffle all the elements in a 2d list then?
for i in range(0,3):
    for j in range(0,3):
        p=randint(0,2)
        q=randint(0,2)
        a[i][j],a[p][q]=a[p][q],a[i][j]
print(a)




for i in range(len(a)):
    for j in range(len(a)):
        p=randint(0,2)
        q=randint(0,2)
        l[i].append(a[p][q])
print(l)



