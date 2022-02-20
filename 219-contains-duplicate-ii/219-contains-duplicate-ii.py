class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)==len(set(nums)):
            return 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] == nums[j] and abs(i - j) <= k):
                    return True
                if(abs(i - j) >= k):
                    break
        return False