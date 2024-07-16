class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
    
        left = 0
        right = x
        medium_idx = (left + right) /2
        while left <= right:
            if medium_idx * medium_idx <= x and (medium_idx + 1) * (medium_idx + 1) > x:
                return medium_idx
            elif medium_idx * medium_idx > x:
                right = medium_idx - 1
            else:
                left = medium_idx + 1
            
            medium_idx = (left + right) / 2