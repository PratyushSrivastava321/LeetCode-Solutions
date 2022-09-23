class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs=0
        for i in range(len(time)):
            time[i]%=60
        dict1={}
        for i in time:
            if (60-i)%60 in dict1:
                pairs+=dict1[(60-i)%60]
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        return pairs
                
            
            
