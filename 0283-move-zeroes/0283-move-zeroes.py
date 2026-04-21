class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums1=[]
        count=0
        for i in range(len(nums)):
            if nums[i]== 0:
                count+=1
            else:
                nums1.append(nums[i])
        for i in range(count):
            nums1.append(0)
        for i in range(len(nums)):
            nums[i]=nums1[i]
                
        