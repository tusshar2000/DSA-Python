#https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

answer = 1 

def findMaxDepth(node, depth):
    global answer
    if node.left:
        answer = max(answer, depth + 1)
        findMaxDepth(node.left, depth + 1)
    if node.right:
        answer = max(answer, depth + 1)
        findMaxDepth(node.right, depth + 1)
    return answer

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        global answer
        answer = 1
        return findMaxDepth(root, 1)
        