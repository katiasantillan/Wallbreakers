class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        w = list(word)
        u = 0
        l = 0
        
        for i in word:
            if(i.isupper()):
                u+=1
            if(i.islower()):
                l+=1
        if(l == 0 or u == 0):
            return(True)
        elif(u == 1 and w[0].isupper()):
            return(True)
        else:
            return(False)