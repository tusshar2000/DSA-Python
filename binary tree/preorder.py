# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

#iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        nodeStack = []
        ansValues = []
        
        nodeStack.append(root)
        
        while len(nodeStack) > 0:
            
            thisNode = nodeStack.pop()
            ansValues.append(thisNode.val)
            
            # we append right and then left because when we pop from the stack then left 
            # node is popped first.
            if thisNode.right:
                nodeStack.append(thisNode.right) 
            if thisNode.left:
                nodeStack.append(thisNode.left)
        
        return ansValues


#recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        
        def solver(stack, node):
            if node:
                stack.append(node.val)
                solver(stack, node.left)
                solver(stack, node.right)
            
        solver(stack, root)
        
        return stack