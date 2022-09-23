class Solution:
    def reverse(self, x: int) -> int:
        if(x==0):
            return 0
        elif(x>0):
            a=int(str(x)[::-1].strip('0'))
            if(2147483647>a):
                return a
            return 0
        else:
            a= -int(str(x)[::-1][:-1].strip('0'))
            if(-2147483648<a):
                return a
            return 0
