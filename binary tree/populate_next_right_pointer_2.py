#https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        def populateNextRightPointer(node):
            if not node:
                return
            
            if node.left and node.right:
                node.left.next = node.right
            
            temp = node
            while temp.next:
                if node.right:
                    if temp.next.left:
                        node.right.next = temp.next.left
                        break
                    elif not temp.next.left and temp.next.right:
                        node.right.next = temp.next.right
                        break
                        
                elif not node.right and node.left:
                    if temp.next.left:
                        node.left.next = temp.next.left
                        break
                    elif not temp.next.left and temp.next.right:
                        node.left.next = temp.next.right
                        break
                        
                temp = temp.next
            if node.right:
                populateNextRightPointer(node.right)
            if node.left:
                populateNextRightPointer(node.left)
    
        populateNextRightPointer(root)
        return root