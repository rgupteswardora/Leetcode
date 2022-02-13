class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num=x
        st=str(num)
        if(num<-2147483648 or num>2147483647):
            return 0
        elif(num>0):
            if(int(st[::-1])<-2147483648 or int(st[::-1])>2147483647):
                return 0
            else:
                return int(st[::-1])
        else:
            st=st.replace('-', '')
            if(int(st[::-1])<-2147483648 or int(st[::-1])>2147483647):
                return 0
            else:
                return int(st[::-1])*-1