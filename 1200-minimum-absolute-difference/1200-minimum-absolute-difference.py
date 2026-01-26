class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        mindiff = float('inf')
        arr2=[]
        arr.sort()
        for i in range(len(arr)-1):
            if(arr[i]<arr[i+1]):
                diff=abs(arr[i+1]-arr[i])
                if mindiff>diff:
                    mindiff=diff
                    arr2 = [[arr[i], arr[i+1]]]
                elif mindiff==diff:
                    arr2.append([arr[i],arr[i+1]])
        return arr2
        
