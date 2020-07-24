# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/

#iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        nodeStack = []
        ansValues = []
        
        nodeStack = [root]
        
        while len(nodeStack) > 0:
            curr = nodeStack.pop()
            ansValues.insert(0,curr.val)
            
            if curr.left:
                nodeStack.append(curr.left)
            
            if curr.right:
                nodeStack.append(curr.right)
            
                
        return ansValues