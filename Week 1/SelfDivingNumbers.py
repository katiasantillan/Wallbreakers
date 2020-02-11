class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        
        for i in range(left, right+1):
            if (len(str(i)) == 1):
                res.append(i)
            else:
                aux = set(str(i))

                while(aux):
                    el = int(aux.pop())
      
                    if(el == 0 or (i%el) != 0):
                        break
      
                    if(not aux):
                        res.append(i)
      
        return(res)