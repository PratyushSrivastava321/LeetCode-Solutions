class Solution:
    def rotate(self, list1: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len1=len(list1[0])
        i=0
        j=0
        while(i<len1 and j<len1):
            i1=i
            j1=j
            while(j1<len1):
                list1[i1][j1],list1[j1][i1]=list1[j1][i1],list1[i1][j1]
                j1+=1
            i+=1
            j+=1
        for i in range(len1):
            list1[i]=list1[i][::-1]
        
                
            
