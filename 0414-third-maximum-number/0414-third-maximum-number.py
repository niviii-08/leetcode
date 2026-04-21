class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ft = sec = th = None  
        for num in nums:
            if num==ft or num==sec or num==th:
                continue
            if num is None or num>ft:
                th=sec
                sec=ft
                ft=num
            elif num is None or num>sec:
                th=sec
                sec=num
            elif num is None or num>th:
                th=num
        return th if th is not None else ft 