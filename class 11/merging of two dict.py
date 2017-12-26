import collections
d1={'a':1,'b':2}
d2={'c':3,'d':4}
d3={'e':5,'f':6}
d5={'g':5,'e':6}
d4={}
for d in (d1,d2,d3):
    d4.update(d)

d4.update(d5)
print(d4)

#chain map integrates or encapculate multiple dictionary

c=collections.ChainMap(d1,d2,d3)
print(c.maps)
print(list(c.items()))
print(list(c.values()))

