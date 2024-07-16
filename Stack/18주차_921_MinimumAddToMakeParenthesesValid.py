class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
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
        
        return len(stack)