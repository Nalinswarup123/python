l=[[3,4,5],[9,7,8]]
t=[[]for i in range(len(l[0]))]
print(t)
for i in range(len(t)):
    for j in range(len(l)):
        t[i].append(l[j][i])
print(t)
        
    
