class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_len = len(nums)
        hash = defaultdict(int)
        for num in nums:
            hash[num] = 1
        for result in range(total_len+1):
            if hash[result] == 0:
                return result