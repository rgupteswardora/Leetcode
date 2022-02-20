class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashset={}
        for al in s:
            if al in hashset:
                hashset[al]+=1
            else:
                hashset[al]=1
        res = len(list(set(list(hashset.values())))) == 1
        return res