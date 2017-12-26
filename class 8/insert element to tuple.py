t=()
l=[1]
for i in range(5):
    t=t+(i,)
print(t)
p=[2]
l[0]=l[0]+p[0]
print(l)
