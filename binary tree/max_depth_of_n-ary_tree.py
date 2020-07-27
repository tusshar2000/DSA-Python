https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

#BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        queue = collections.deque([(root,1)])
        while queue:
            node, level = queue.popleft()
            for child in node.children:
                queue.append((child, level + 1))
                
        return level
            