class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        st=''
        num=n
        while(num!=0):
            st=st+str(num%2)
            num=num//2
        st=st+'0'*(32-len(st))
        st=st[::-1]
        nums=0
        print(st)
        for i in range(0,len(st)):
            if st[i] == '1':
                nums=nums+2**i
        return nums