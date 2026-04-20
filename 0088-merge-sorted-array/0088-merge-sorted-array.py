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
        i=0
        j=0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                newbee.append(nums1[i])
                i+=1
            else:
                newbee.append(nums2[j])
                j+=1
        while i < m:
            newbee.append(nums1[i])
            i+=1
        while j<n:
            newbee.append(nums2[j])
            j+=1
        for k in range(m+n):
            nums1[k]=newbee[k]
        return nums1