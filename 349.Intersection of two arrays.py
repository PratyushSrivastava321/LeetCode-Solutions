class Solution:
    def intersection(self, list1: List[int], list2: List[int]) -> List[int]:
        dict1={}
        for i in list1:
            dict1[i]=1
        for j in list2:
            if j in dict1:
                dict1[j]=0
        list3=[]
        for k in dict1:
            if(dict1[k]):
                continue
            else:
                list3.append(k)
        return list3
