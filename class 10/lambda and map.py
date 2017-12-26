cel=[12,42,51]
fah=list(map((lambda x:(float(9)/5)*x+32),cel))
print(fah)
i=list(map(int,fah))
print(i)
b=[2,4]
d=list(map(lambda x,y:x+y, cel,b))
print(d)
