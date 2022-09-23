class Solution:
    def intersect(self, list1: List[int], list2: List[int]) -> List[int]:
        dict1={}
        dict2={}
        for i in list1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for j in list2:
            if j in dict2:
                dict2[j]+=1
            else:
                dict2[j]=1
        
        list3=[]
        # print(dict1,dict2)
        for k in dict2:
            if(k in dict1):
                min1=min(dict2[k],dict1[k])
                for _ in range(min1):
                    # print(_)
                    list3.append(k)
        return list3
