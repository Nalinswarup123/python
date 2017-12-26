graph={'A':['E','B','D'],
       'B':['A','D','C'],
       'C':['B'],
       'D':['A','B'],
       'E':['A']}
def bfs_connected_component(graph,start):
    visited=[]
    queue=[start]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue=queue+graph[node]
            print(queue)
    return visited
print(bfs_connected_component(graph,'B'))
