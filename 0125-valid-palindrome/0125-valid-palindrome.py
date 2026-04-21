class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        filtered=[c.lower() for c in s if c.isalnum()]
        leng=len(filtered)
        for i in range(leng//2):
            j=leng-1-i
            if filtered[i]!=filtered[j]:
                return False
        return True