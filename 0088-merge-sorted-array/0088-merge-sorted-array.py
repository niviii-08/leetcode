class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 and nums2:
            return 0
        newbee=[]
        k=0
        for i in range(m):
                newbee.append(nums1[i])
                k+=1
        for j in range(n):
            newbee.append(nums2[j])
            k+=1
        newbee.sort()
        for i in range(k):
            nums1[i]=newbee[i]