d={'vamsi':'bc','nalin':'chutiya','nalin':'9','akanksha':'sarjaa','akanksha':'marjaa'}
print(max(d.values()))
print(d.items())
print(sorted(d.values()))

#s={(0,3):1,(2,1):2,(4,4):3}
#print(s[(4,4)])
print(sorted(zip(d.values(),d.keys())))
print(min(d.values()))
d['vamsi']='mc'
print(d.items())
l=['1','2','3']
b=''.join(l)
print(b)
l.extend(['4','5'])
print(l)
l.append(['6','7'])
print(l)
