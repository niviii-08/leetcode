class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        imbalance = 0  
        open_brackets = 0
        for ch in s:
            if ch == '[':
                open_brackets += 1
            else: 
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    imbalance += 1
        return (imbalance + 1) // 2