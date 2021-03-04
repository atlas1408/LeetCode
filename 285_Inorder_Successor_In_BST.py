# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def rec(node):
            nonlocal parent
            if not node:
                return
            if node == p:
                return
            if node.val< p.val:
                rec(node.right)
                if node.val > p.val:
                    if not parent:
                        parent = node
                return
            else:
                rec(node.left)
                if node.val > p.val:
                    if not parent:
                        parent = node
                return
        parent = None
        if p.right:
            parent = p.right
            while parent.left:
                parent = parent.left
            return parent    
        rec(root)
        return parent