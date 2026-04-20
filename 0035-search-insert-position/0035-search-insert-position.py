class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        i=0
        while i < len(nums):
            if(nums[i]==target):
                return i
            else:
                i+=1
        l=len(nums)
        if target<nums[0]:
                return 0
        if target>nums[l-1]:
                return l  
        for i in range(0,l-1):
            if nums[i]<target and target<nums[i+1]:
                return i+1