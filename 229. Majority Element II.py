class Solution:
    def majorityElement(self, list1: List[int]) -> List[int]:
        len1=len(list1)
        len2=(len1//3 )+1
        dict1={}
        res=[]
        set1=set()
        for i in list1:
            if(i in dict1):
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in dict1:
            if(dict1[i]>=len2):
                res.append(i)
        return res
        
