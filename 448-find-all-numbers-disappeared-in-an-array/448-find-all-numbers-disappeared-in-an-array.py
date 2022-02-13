class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashset=set()
        for i in range(1,len(nums)+1):
            hashset.add(i)
        for j in nums:
            if j in hashset:
                hashset.remove(j)
        return hashset