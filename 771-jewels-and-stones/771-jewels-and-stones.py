class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        hashset=set(jewels)
        count=0
        for i in stones:
            if i in hashset:
                count+=1
        return count