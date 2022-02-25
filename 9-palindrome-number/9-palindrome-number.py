class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #121 121
        #345 543
        st=str(x)
        if st==st[::-1]:
            return True
        return False
        
        
        