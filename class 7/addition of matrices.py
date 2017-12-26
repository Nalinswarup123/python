l1=[[1,2,3],[4,5,6],[7,8,9]]
a=[[5,8],[2,4],[1,3]]
b=[[7,8,9],[4,1,3]]
l2=[[11,12,13],[4,4,8],[8,9,69]]
l3=[[] for i in range(len(l1))]
for i in range(3):
    for j in range(3):
        l3[i].append(l1[i][j]+l2[i][j])

print(l1)
print(l3)

l4=[[] for i in range(len(l1))]
for i in range(l1):
