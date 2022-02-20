class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        hashset=set(allowed)
        count=0
        b=0
        for i in words:
            checkset=set(i)
            for j in checkset:
                if j in hashset:
                    b=b+1
            if(b==len(checkset)):
                count+=1
            b=0
        return count