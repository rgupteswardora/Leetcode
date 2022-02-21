class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        nums.sort()
        count=0
        max=0
        num=0
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        sorted_x = sorted(hashmap.items(), key=lambda kv: kv[1])
        return sorted_x[-1][0]