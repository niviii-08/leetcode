class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        def dp(index, current_sum):
            if index == len(nums):
                if current_sum == target:
                    return 1
                return 0
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            add = dp(index + 1, current_sum + nums[index])
            subtract = dp(index + 1, current_sum - nums[index])
            memo[(index, current_sum)] = add + subtract
            return memo[(index, current_sum)]
        return dp(0, 0)