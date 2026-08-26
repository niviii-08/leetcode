class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        curr=nums[0]
        max1=nums[0]
        for i in range(1,len(nums)):
            curr=max(nums[i],curr+nums[i])
            max1=max(max1,curr)
        return max1
