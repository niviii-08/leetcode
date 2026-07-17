class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max1 = max(nums)
        freq = [0] * (max1 + 1)
        for x in nums:
            freq[x] += 1
        cnt = [0] * (max1 + 1)
        for d in range(1, max1 + 1):
            for multiple in range(d, max1 + 1, d):
                cnt[d] += freq[multiple]
        exact = [0] * (max1 + 1)
        for d in range(max1, 0, -1):
            c = cnt[d]
            exact[d] = c * (c - 1) // 2
            for multiple in range(2 * d, max1 + 1, d):
                exact[d] -= exact[multiple]
        prefix = []
        values = []
        total = 0
        for g in range(1, max1 + 1):
            if exact[g] > 0:
                total += exact[g]
                prefix.append(total)
                values.append(g)
        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(values[idx])
        return ans