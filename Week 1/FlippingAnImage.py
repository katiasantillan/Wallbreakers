class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(A)):

            A[i] = [ 0 if i == 1 else 1 for i in A[i][::-1]]
        
        return A