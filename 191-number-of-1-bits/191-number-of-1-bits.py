class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        st=''
        num=n
        count=0
        while(num!=0):
            st=st+str(num%2)
            num=num//2
        for i in st:
            if i=='1':
                count+=1
        return count