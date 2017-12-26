for i in range(1,8):
    if(i<5):print('*'*i)
    else:print('*'*(8-i))


k=1
for i in range(4,0,-1):
    print(' '*(i-1)+'* '*k)
    k+=1
    


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(5)
f(4,[3,2,1])
f(3)
f(2,[3,1])
'''
l=[1,2,3,4,5]
l=[8,9]
print(l)
p=[]
p.append(1)
p.append(4)
print(p)
p=[]
p.append(0)
print(p)'''


