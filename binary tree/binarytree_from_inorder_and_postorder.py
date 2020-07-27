#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def makeTree(postorder, inorder):
            
            if len(postorder) == 0:
                return None 
            
            root = TreeNode(postorder[-1])
            rootIndex = inorder.index(postorder[-1])
            
            leftInorder = inorder[ : rootIndex]
            rightInorder = inorder[rootIndex + 1 : ]
            
            leftPostorder = postorder[ : rootIndex]
            rightPostorder = postorder[rootIndex : len(postorder)-1]

            root.left = makeTree(leftPostorder, leftInorder)
            root.right = makeTree(rightPostorder, rightInorder)
            
            return root
               
        return makeTree(postorder, inorder)