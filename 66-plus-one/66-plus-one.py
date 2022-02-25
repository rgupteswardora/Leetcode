class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #  num=99==>99+1===100
        returnlist=[]
        num=''
        for i in digits:
            num=num+str(i)
        retnum=int(num)+1
        retnum=str(retnum)
        for i in retnum:
            returnlist.append(int(i))
        return returnlist
            