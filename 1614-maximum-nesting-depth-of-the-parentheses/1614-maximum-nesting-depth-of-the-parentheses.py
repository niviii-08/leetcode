class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_depth = 0
        current = 0
        for ch in s:
            if ch == '(':
                current += 1
                max_depth = max(max_depth, current)
            elif ch == ')':
                current -= 1
        return max_depth