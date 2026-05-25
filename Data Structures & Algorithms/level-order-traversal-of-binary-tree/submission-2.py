# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []
        if not root:
            return level_order
        from collections import deque
        q = deque([root])
        while q:
            level = []
            i = 0
            n = len(q)
            while i < n:
                node = q.popleft()
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                i += 1
            level_order.append(level[:])
        return level_order