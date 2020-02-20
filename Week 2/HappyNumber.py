class Solution:
    def isHappy(self, n: int) -> bool:
        suma = 0
        s = set()
        while(n != 1):

            nAux = list(str(n))

            for i in nAux:
                suma+= int(i)**2

            n = suma
            
            if(suma not in s):
                s.add(suma)
            else:
                return False
            suma = 0
        
        return True