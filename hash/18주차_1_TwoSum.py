class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = defaultdict(int)
        for idx, num in enumerate(nums):
            if num in hash:
                return [hash[num], idx]
            hash[target - num] = idx
