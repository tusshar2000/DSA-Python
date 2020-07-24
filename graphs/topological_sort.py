# https://leetcode.com/problems/course-schedule-ii

from collections import *
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        graph = {i:[] for i in range(numCourses)}
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        
        visited = [0]*numCourses
        is_possible = True
        path = []
        
        def toposort(visited, node, path):
            nonlocal is_possible
            
            if is_possible == False:
                return
            
            visited[node] = 1
            
            for neighbour in graph[node]:
                if visited[neighbour] == 0:
                    toposort(visited, neighbour, path)
                if visited[neighbour] == 1:
                    is_possible = False
            
            visited[node] = 2
            path.append(node)
        
        for node in range(numCourses):
            if visited[node] == 0 and is_possible == True:
                toposort(visited, node, path)
        
        if is_possible:
            return path[::-1]
        return []
            
                    