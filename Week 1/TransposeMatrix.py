class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if(A):
            transpose, auxRow, i = [], [], 0

            while(i < len(A[0])):

                for j in A:
                    auxRow.append(j[i])

                transpose.append(auxRow)
                auxRow = []
                i+=1

            return transpose
        return A