class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val1=0
        index=[]
        len1=len(nums)
        for i in range(len1):
            if(nums[i]==val):
                val1+=1
                index.append(i)
        for j in index[::-1]:
            del nums[j]
        for i in range(val1):
            nums.append("_")
        return len1-val1
