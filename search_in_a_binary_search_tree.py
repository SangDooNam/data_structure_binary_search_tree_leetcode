from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        elif root.val == val:
            return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)
                
                
class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        
        queue = deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.val == val:
                    return node
                
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return None