from random import *
l=[1,5,7,8,6,2,4,5,6]
p=0
q=[11,12,21]
l[4]=7
z=[]
l.append(q)
l.append(24)
while(p!=len(l)):
    print(l[p])
    p+=1
shuffle(q)
print(q)

h=[i*0.5 for i in range(10) if i * 0.5 < 3.5]  #list comprehension
print(h)
a=[8,9]
q.extend(a)
print('ext=',q)
a.insert(1,50)
print('a=',a)
y=a.pop(1)
print('y=',y)
a.reverse()
print(a)
s='hii there'
a=s.split()
print(a)
t=[4,8,6,1,2]
t.sort()
print(t)
