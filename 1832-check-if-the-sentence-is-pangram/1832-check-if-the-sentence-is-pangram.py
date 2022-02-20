class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        checkset=set("thequickbrownfoxjumpsoverthelazydog")
        hashset=set(sentence)
        if(len(checkset)==len(hashset)):
            return True
        return False