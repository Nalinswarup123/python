import collections

d=collections.defaultdict(lambda:'key not found')
d['a']=1
d['b']=2
d['c']=3
print(d['a'])
print(d['e'])



f=lambda x,y:print('hii',x)
f(1,2)

