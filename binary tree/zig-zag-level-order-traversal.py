# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return None
        
        queue = [root]               #queue is used to keep track of nodes at current level.   
        level = 1                    #because we use current level for deriving answer of                                        #next level, so assigned level=1 and not level=0.
        path = [[root.val]]          #this maintains our answer.
        
        while True:
            
            this_level_path = []     #for storing nodes of the next level. 
            
            for node in queue:
                if node.left:
                    this_level_path.append(node.left)
                if node.right:
                    this_level_path.append(node.right)
            
            if not this_level_path:  #if this is the last level then we exit.
                break
            
            if level%2==1:           #if level is odd then add answer in reverse.
                path.append([node.val for node in this_level_path][::-1])
            else:
                path.append([node.val for node in this_level_path])
            
            queue = this_level_path  #assign next level nodes to the queue making it current                                      #level for the next iteration and loop over again.
            level += 1               #obvious!
        
        return path                  #we made it.