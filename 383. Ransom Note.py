class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1={}
        for i in ransomNote:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for j in magazine:
            if j in dict1:
                if(dict1[j]==0):
                    continue
                dict1[j]-=1
        len1=len(dict1)
        for k in dict1:
            if(dict1[k]):
                return False
        return True
