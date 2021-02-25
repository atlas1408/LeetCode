import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levels = [[root.val]]
        queue = collections.deque([root])
        i = len(queue)
        while queue:
            temp = []
            for _ in range(i):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    temp.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    temp.append(curr.right.val)
            if temp:
                if len(levels)%2 != 0:
                    temp = temp[::-1]
                levels.append(temp)
            i = len(queue)
        return levels