class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        newnums=[]
        for i in nums:
            newnums.append(i)
        for i in range(len(nums)):
            nums[(i+k)%len(nums)]=newnums[i]
            