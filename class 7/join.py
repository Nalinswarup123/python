l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[11,12,13],[4,4,8],[8,9,69]]
l3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        l3[i][j]=l1[i][j]+l2[i][j]
        l1[i][j]=l1[i][j]+l2[i][j]

print(l1)
print(l3)
