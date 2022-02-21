class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset={}
        for i in nums:
            if i in hashset:
                hashset[i]+=1
            else:
                hashset[i]=1
        marklist = sorted(hashset.items(), key=lambda x:x[1])
        return marklist[-1][0]