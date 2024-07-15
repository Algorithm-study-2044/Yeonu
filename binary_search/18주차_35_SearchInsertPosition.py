class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_len = len(nums)
        left = 0
        right = total_len - 1
        medium = (left + right) / 2
        while left <= right:
            if nums[medium] == target:
                return medium
            if medium == 0 and nums[medium] < target:
                left = medium + 1
            if medium == 0 and nums[medium] >= target:
                return medium
            if medium == total_len - 1 and nums[medium] < target:
                return medium + 1
            if medium == total_len - 1 and nums[medium] > target:
                right = medium - 1
            if nums[medium] > target and nums[medium - 1] < target:
                return medium
            if nums[medium] > target:
                right = medium - 1
            else:
                left = medium + 1
            medium = (right + left) / 2