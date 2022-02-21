class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashset={}
        rt=[]
        for i in nums:
            if i in hashset:
                hashset[i]+=1
            else:
                hashset[i]=1
        for i in hashset.keys():
            if(hashset[i]>1):
                rt.append(i)
        return rt
        