class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return None
        i=0
        curr=0
        num=0
        l=len(digits)-1
        while i<len(digits):
            curr=digits[i]*pow(10,l)
            num+=curr
            i+=1
            l-=1
        newn=num+1
        digits = [int(d) for d in str(newn)]
        return digits
