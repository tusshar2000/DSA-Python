# https://leetcode.com/problems/course-schedule/

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # defaultdict(list) makes work easier
        graph = defaultdict(list)
        
        # we need to have every node in our graph as a key even though there might be not
        # any connection to it/ it is not a connected graph. Just a basic and easy                   # preparation.
        graph = {node:[] for node in range(numCourses)} 
        
        # now we add the edges in reverse manner because input is given in that format.
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        is_possible = True
        visited = [0]*(numCourses)
        
        # note that we will be using 0,1,2 values for representing the state of our node
        # in visited list.
        # value 0 represents node is unprocessed.
        # value 1 represents node is under process.
        # value 2 represents node is processed.
        
        def dfs(visited, node):
            nonlocal is_possible
            
            visited[node] = 1 
            
            for neighbour in graph[node]:
                
                if visited[neighbour] == 0:
                    dfs(visited, neighbour)
                
                # this is the condition where we find if a cycle exsits or not.
                # if our neighbour node has a value 1 in visited list, it means that
                # this node was still under process and we found another way through
                # which we can access this, meaning we found a cycle.
                if visited[neighbour] == 1:
                    is_possible = False
                    
            visited[node] = 2
        
        # now for every node we check if it is unprocessed then call dfs for it,
        # this way we are assured even if our graph in not fully connected we will
        # be processing it.
        
        for node in range(numCourses):
            # I added another condition to check is_possible is still true then only
            # process the node, as is_possible variable False value represents that
            # our graph has cycle, so basically no need to process any node further.
            if visited[node] == 0 and is_possible==True:
                dfs(visited, node)
                
        return is_possible