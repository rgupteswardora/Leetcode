class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rt=[]
        count=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(i==j):
                    None
                elif(nums[i]>nums[j]):
                    count+=1
            rt.append(count)
            count=0
        return rt
                    