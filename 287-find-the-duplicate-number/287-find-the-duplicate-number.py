class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        se=set()
        for i in nums:
            if i not in se:
                se.add(i)
            else:
                return i