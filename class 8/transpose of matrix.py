l=[[1,2],[3,4],[5,6]]
def trans(l):
    t=[]
    for i in range(len(l[0])):
        t.append([])
    for i in range(len(t)):
        for j in range(len(l)):
            t[i].append(l[j][i])
    print(t)

trans(l)
s="""asdfsgfdh
hjvj"""
print(s)







            
