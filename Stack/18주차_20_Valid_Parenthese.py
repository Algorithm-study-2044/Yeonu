from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = deque()
        for bracket in s:
            if len(stack) > 0:
                target = stack.pop()
                if target in hash and bracket == hash[target]:
                    continue
                stack.append(target)
            stack.append(bracket)
        
        if len(stack) > 0:
            return False
        else:
            return True
        