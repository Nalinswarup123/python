n=int(input('enter no of vertices'))
nodes=[]
edges={}
print('ener vertices: ')
for i in range(n):
    nodes.append(input('enter %d vertex: '%i))
    edges[nodes[i]]=[]
print('enter edges: ')
while True:
    choice=int(input('enter 1 to add edge and 0 to break: '))
    if choice==0:
        break
    else:
        src=input('enter source vertex: ')
        dest=input('enter destination vertex: ')
        if not(src in nodes or dest in nodes):
            raise ValueError('node not in graph')
        else:
            edges[src].append(dest)
print('graph is: ')
for i in nodes:
    for j in edges[i]:
        print(i+' --> ' +j)
