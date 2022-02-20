class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        le=len(nums)
        while(i!=le):
            if(nums[i]==val):
                nums.pop(i)
                le=len(nums)
            else:
                i+=1
        return len(nums)