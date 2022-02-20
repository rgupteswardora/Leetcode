class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset={}
        sum=0
        for i in nums:
            if (i in hashset): 
                hashset[i] += 1
            else: 
                hashset[i] = 1
        for keys in hashset.keys():
            if hashset[keys]==1:
                sum=sum+keys
        return sum