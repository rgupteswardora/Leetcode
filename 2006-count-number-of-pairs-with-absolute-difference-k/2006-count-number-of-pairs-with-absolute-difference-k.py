class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        for i in range(0,len(nums)):
            for j in range (i+1,len(nums)):
                if(abs(nums[i]-nums[j])==k):
                    count+=1
        return count