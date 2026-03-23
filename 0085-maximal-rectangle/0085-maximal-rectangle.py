class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for row in matrix:
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            stack = []
            for i in range(cols + 1):
                h = heights[i] if i < cols else 0
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    if not stack:
                        width = i
                    else:
                        width = i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
        return max_area