class Solution:
    def findComplement(self, num: int) -> int:

        aux = ['0' if i == '1' else '1' for i in bin(num)[2:]]

        aux = int(('').join(aux),2)
        return(aux)
