class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        vals = set()
        for n in nums:
            if n in vals:
                return True
            else:
                vals.add(n)
        return False