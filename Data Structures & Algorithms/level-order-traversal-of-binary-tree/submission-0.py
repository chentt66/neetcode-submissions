# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []
        if root is None:
            return level_order
        from collections import deque
        q = deque([root])
        # Issue: while q is not None. deque([]) is not None is always True.
        while len(q) > 0:
        # OR: while q
            n = len(q) # important
            level = []
            for i in range(n):
                node = q[0]
                level.append(node.val)
                q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            level_order.append(level[:])
        return level_order
