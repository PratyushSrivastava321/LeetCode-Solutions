class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max1=len(nums)
        sum1=max1*((max1+1)/2)
        for i in nums:
            sum1-=i
        return int(sum1)
