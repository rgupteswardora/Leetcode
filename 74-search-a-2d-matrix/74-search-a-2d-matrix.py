class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        lis=[]
        for i in matrix:
            lis=lis+i
        if target in lis:
            return True
        else:
            return False