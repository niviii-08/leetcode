class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        i=0
        j=0 
        while i < len(haystack):
            if haystack[i]==needle[j]:
                j+=1
                if j==len(needle):
                    return i-j+1
            else:
                i=i-j
                j=0
            i+=1
        return -1