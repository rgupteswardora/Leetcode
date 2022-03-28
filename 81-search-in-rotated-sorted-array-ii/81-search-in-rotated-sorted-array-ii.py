class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        se=set(nums)
        if target in se:
            return True
        return False