class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        rich=[]
        for i in range(len(accounts)):
            high=0
            for j in range(len(accounts[i])):
                high+=accounts[i][j]
            rich.append(high)
        l=0
        for k in range(len(rich)):
            if l<rich[k]:
                l=rich[k]
        return l