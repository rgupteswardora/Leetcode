class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset=set()
        for i in nums:
            if i in hashset:
                hashset.remove(i)
            else:
                hashset.add(i)
        num=list(hashset)
        return num[0]
        