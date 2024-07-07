# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        def dfs(node, depth):
            if node is None:
                return

            depth += 1
            result[0] = max(result[0], depth)
            
            if node.left is None and node.right is None:
                return
            
            if node.left is not None:
                dfs(node.left, depth)
            
            if node.right is not None:
                dfs(node.right, depth)
        
        dfs(root, 0)

        return result[0]
        