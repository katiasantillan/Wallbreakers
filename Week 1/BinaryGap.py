class Solution:
    def binaryGap(self, N: int) -> int:
        binN = bin(N)[2:]
        aux = []
        maxV = 0

        for i in range(len(binN)):
            if(binN[i] == '1'):
                aux.append(i)
      
        for i in range(len(aux)-1):
            if(abs(aux[i+1]-aux[i]) > maxV):
                maxV = abs(aux[i+1]-aux[i])

        return(maxV)