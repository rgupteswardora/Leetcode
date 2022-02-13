class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index=-1
        found=0
        for i in range(0,len(nums)):
            if(target==nums[i]):
                found=1
                index=i
                exit
        if(found==1):
            return index
        else:
            return index