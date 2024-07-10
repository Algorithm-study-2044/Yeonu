class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev_num = 0
        for roman in s[::-1]:
            cur_num = hash[roman]
            if prev_num <= cur_num:
                result += cur_num
            else:
                result -= cur_num
            prev_num = cur_num
        
        return result
        