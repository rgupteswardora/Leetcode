class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(0,len(nums)):
            if(nums[r]!=0):
                nums[l],nums[r]=nums[r],nums[l]
                l+=1