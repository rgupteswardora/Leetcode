class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le=len(nums)
        su=(le*(le+1))/2
        sum=0
        for i in nums:
            sum=sum+i
        return abs(sum-su)
        