class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        s=prices[0]
        m=0
        for i in prices:
            if i < s :
                s=i
            else:
                m=max(m,i-s)
        return m 