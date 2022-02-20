class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        haahset=set(nums)
        i=0
        while(i!=1):
            if original in haahset:
                original=original*2
            else:
                i=1
        return original
        