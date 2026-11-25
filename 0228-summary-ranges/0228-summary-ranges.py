class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if len(nums) == 0:
            return result
        str1 = str(nums[0])
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                if "->" not in str1:
                    str1 = str1 + "->"
            else:
                if "->" in str1:
                    str1 = str1 + str(nums[i-1])
                result.append(str1)
                str1 = str(nums[i])
        if "->" in str1:
            str1 = str1 + str(nums[-1])
        result.append(str1)
        return result