# https://leetcode.com/problems/minimum-depth-of-binary-tree

#DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        answer = float("inf")
        def min_height(node, height):
            nonlocal answer
            if node.left:
                min_height(node.left, height+1)
            if node.right:
                min_height(node.right, height+1)
            if not node.left and not node.right:
                answer = min(answer, height)
        
        min_height(root, 1)
        return answer

# BFS   

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque([(root,1)])
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))