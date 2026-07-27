class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        i=0
        maxarea=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            if area>maxarea:
                maxarea=area
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
            i+=1
        return maxarea
        
