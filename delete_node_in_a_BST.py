from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key):
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            min_val = self.find_mid(root.right)
            root.val = min_val.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root
        
    def find_mid(self, node):
        while node.left:
            node = node.left
        return node


def create_binary_tree(elements):
    if not elements:
        return None

    root = TreeNode(elements[0])
    queue = deque([root])
    idx = 1
    n = len(elements)
    while idx < n:
        node = queue.popleft()
        if node:
            
            if idx < n and elements[idx] is not None:
                node.left = TreeNode(elements[idx])
                queue.append(node.left)
            idx += 1
            if idx < n and elements[idx] is not None:
                node.right = TreeNode(elements[idx])
                queue.append(node.right)
            idx += 1
    return root


def print_binary_tree(root):
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        n = len(queue)
        result = []
        
        for _ in range(n):
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('None')
            
        while result and result[-1] == 'None':
            result.pop()
        
        if result:
            print(' '.join(result), end=' ')
    print()
    
root = [5,3,6,2,4,None,7]
key = 3
root = [5,3,6,2,4,None,7]
key = 0 

root = create_binary_tree(root)
sol = Solution()

root = sol.deleteNode(root, key)

print_binary_tree(root)