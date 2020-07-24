#find all paths between 2 node using dfs.

#method 1
graph = {1:[2,3], 2:[3,4], 3:[1,4], 4:[2,3]}

def dfs(start, end, visited, paths, path=[]):
    visited.add(start)
    path = path + [start]
    if start == end:
        #store a copy of path and not actual path because we make 
        #changes to a certain path which are reflected here.
        paths.append(path[:])
    else:
        for neigh in graph[start]:
            if neigh not in visited:
                dfs(neigh, end, visited, paths, path)
        
    path.pop()
    visited.remove(start)

paths = []
visited = set()
dfs(1, 4, visited, paths)
print(paths)

#method 2
def allPathsSourceTarget(self, graph):  
    def dfs(formed):
        if formed[-1] == n - 1:
            sol.append(formed)
            return      
        for child in graph[formed[-1]]:
            dfs(formed + [child])
                
sol, n = [], len(graph)            
dfs([0])
print(sol)