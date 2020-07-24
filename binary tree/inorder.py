# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/

#recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def solver(stack, node):
            if node:
                solver(stack, node.left)
                stack.append(node.val)
                solver(stack, node.right)
        
        stack = []
        solver(stack, root)
        
        return stack

#iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        nodeStack = []
        ansValues = []
        
        while True:
            while root:
                nodeStack.append(root)
                root = root.left
            
            if not nodeStack:
                break
            
            temp = nodeStack.pop()
            ansValues.append(temp.val)
            root = temp.right
        
        return ansValues