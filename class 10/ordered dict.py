import collections

print('This is a dict:\n')
d={}
d['a']=1
d['b']=2
d['c']=3
d['d']=4
print(d)
for key, value in d.items():
    print(key,value)

print('\nThis is an ordered dict:\n')
od=collections.OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
for key , value in od.items():
    print(key,value)
