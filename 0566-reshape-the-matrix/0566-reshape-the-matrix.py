class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat) * len(mat[0]) != r * c:
            return mat
        arr=[]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                arr.append(mat[i][j])
        result = []
        for i in range(r):
            result.append(arr[i*c:(i+1)*c])
        return result

