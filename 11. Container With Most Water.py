class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        i=0
        j=len(height)-1
        while(i<j):
            if(height[i]<height[j]):
                result=height[i]*(j-i)
                i+=1
            else:
                result =height[j]*(j-i)
                j-=1
            if(result>res):
                res=result
            # print(result)
        return res
# def maxArea(self, H: List[int]) -> int:
#         ans, i, j = 0, 0, len(H)-1
#         while (i < j):
#             if H[i] <= H[j]:
#                 res = H[i] * (j - i)
#                 i += 1
#             else:
#                 res = H[j] * (j - i)
#                 j -= 1
#             if res > ans: ans = res
#         return ans
