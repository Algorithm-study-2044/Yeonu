from collections import deque
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s = deque(s)
        stack_t = deque(t)

        def preprocess(input_uni):
            input_str = deque(input_uni)
            stack = deque()
            while input_str:
                target = input_str.popleft()
                if target == '#' and stack:
                    stack.pop()
                elif target == '#':
                    continue
                else:
                    stack.append(target)
            return stack
        
        stack_s = preprocess(s)
        stack_t = preprocess(t)

        if stack_s == stack_t:
            return True
        else:
            return False