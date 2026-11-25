class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        for i in range(len(arr) - m * k + 1):
            count = 0

            for j in range(m * k):
                if arr[i + j] == arr[i + j % m]:
                    count += 1
                else:
                    break

            if count == m * k:
                return True

        return False
