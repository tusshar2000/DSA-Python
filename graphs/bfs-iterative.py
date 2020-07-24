from collections import *
graph = {0:[2,3], 1:[0], 2:[1,3], 3:[1,4], 4:[1,0]}

queue = deque()
queue.append(1)
visited = {1}
path=[]
while queue:
    node = queue.popleft()
    path.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour) 
            queue.append(neighbour)
print(path)