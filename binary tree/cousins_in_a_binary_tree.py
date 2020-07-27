# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        queue = collections.deque([(root, 1)])
        depth = {root: 1}
        parent = {root: None}
        node_x = None
        node_y = None
        
        while queue:
            node, level = queue.popleft()
            if node.val == x:
                node_x = node 
            if node.val == y:
                node_y = node
            
            if node.left:
                depth[node.left] = level + 1
                parent[node.left] = node
                queue.append((node.left, level + 1))
            if node.right:
                depth[node.right] = level + 1
                parent[node.right] = node
                queue.append((node.right, level + 1))
            
            if node_x and node_y:
                if depth[node_x] == depth[node_y]:
                    if parent[node_x] != parent[node_y]:
                        return True
                return False