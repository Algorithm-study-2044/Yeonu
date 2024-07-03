      
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob_1 = sum(nums[0::2])
        rob_2 = sum(nums[1::2])

        if rob_1 > rob_2:
            return rob_1
        else:
            return rob_2

solution = Solution()
nums = [2,7,9,3,1]
print(solution.rob(nums))        