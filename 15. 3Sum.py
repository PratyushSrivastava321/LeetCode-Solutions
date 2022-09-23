class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total==0:
                    triplet=[nums[i],nums[l],nums[r]]
                    res.add(tuple(triplet))
                    l+=1                    
                elif total<0:
                    l+=1
                else:
                    r-=1
        return res
