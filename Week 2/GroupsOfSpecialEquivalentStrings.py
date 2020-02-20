class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        auxA = set([('').join(sorted(i[1::2])+sorted(i[::2])) for i in A]) 


        return(len(auxA))