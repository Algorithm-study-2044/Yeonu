# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        # 값이 없으면 0 반환
        if not root:
            return 0
        # high보다 크면 왼쪽에 있는 값만 더하기
        if root.val > high:
        	return self.rangeSumBST(root.left, low, high)
		# low보다 작으면 오른쪽에 있는 값만 더하기
		if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        # low와 high 사이에 있으면 왼쪽, 오른쪽 모두 검사
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)