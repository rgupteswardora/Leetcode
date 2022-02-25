class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if(i[0]<=target and i[-1]>=target):
                left=0
                right=len(i)-1
                while(left<=right):
                    mid=(left+right)//2
                    if left==right and i[mid]!=target:
                        return False
                    if i[mid]==target:
                        return True
                    elif i[mid]>target:
                        right=mid
                    elif i[mid]<target:
                        left=mid+1
            else:
                None
        return False