class Solution:
    def plusOne(self,list1: List[int]) -> List[int]:
        str1=""
        for i in list1:
            str1+=str(i)
        num1=int(str1)+1
        str1=str(num1)
        list1=list(map(int,str1))
        return list1
