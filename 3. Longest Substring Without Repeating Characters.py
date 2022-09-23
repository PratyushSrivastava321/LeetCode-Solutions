class Solution:
    def lengthOfLongestSubstring(self, str1: str) -> int:
        # str1=input()
        dict1={}
        i,j=0,0
        max1=0
        len1=len(str1)
        while(j<len1):
            if str1[j] in dict1:
                if((j-i)>max1):
                    max1=j-i     
    #             print(dict1)
                l=dict1[str1[j]]
                for k in range(i,dict1[str1[j]]+1):
                    del dict1[str1[k]]
                i=l+1
            dict1[str1[j]]=j
            j+=1
        len2=len(dict1)
        if(len2>max1):
            max1=len2
        return max1
