class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str;
        """
        if not strs:
            return ""
        pre=""
        for i in range(len(strs[0])):
            ch=strs[0][i]
            for j in strs:
                if i>=len(j) or j[i]!=ch:
                    return pre 
            pre+=ch
        return pre