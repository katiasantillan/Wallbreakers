from collections import Counter
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = list(J)
        S = list(S)
        c = Counter(S)
        jr = 0

        for i in J:
            if(i in c):
                jr+=c[i]
        return(jr)