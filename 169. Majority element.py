class Solution:
    def majorityElement(self, list1: List[int]) -> int:
        # len1=len(list1)
        # if(len1==1):
        #     return list1[0]
        # len2=int(len1/2)+1
        # dict1={}
        # for i in list1:
        #     if(i in dict1):
        #         dict1[i]+=1
        #         if(dict1[i]==len2):
        #             return i
        #     else:
        #         dict1[i]=1
        len1=len(list1)
        len2=int(len1)+1
        list1.sort()
        return (list1[len1//2])
