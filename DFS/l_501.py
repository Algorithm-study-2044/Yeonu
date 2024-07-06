# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count = {}
        result = []

        def dfs(node):
            if not node:
                return          
            if node.val in count:
                count[node.val]  += 1
            else:
                count[node.val]  = 0

            dfs(node.right)
            dfs(node.left)

        dfs(root)
        max_num = max(count.values())
        for key, item in count.items():
            if item == max_num:
                result.append(key)

        return result
