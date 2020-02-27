class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if(s == ""):
            return True
        
        listS = list(s)
        listT = list(t)
        
        
        for i in listT:
            if(len(listS) == 0):
                return True
            
            if i == listS[0]:
                listS.pop(0)
        
        return(len(listS) == 0)
        