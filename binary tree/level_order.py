# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        def solver(ans, queue):
            child = []
            for node in queue:
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            if child:
                ans.append([i.val for i in child])
                solver(ans, child)
            return 
        
        ans = [[root.val]]
        solver(ans, [root])
        return ans
                