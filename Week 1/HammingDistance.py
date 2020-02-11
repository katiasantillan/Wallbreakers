class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = 0
        for i in bin(x^y)[2:]:
            if(i == '1'):
                c+=1
        return c
        