from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split(" ")
        B = B.split(" ")
        uncommon = []
        counterA = Counter(A)
        counterB = Counter(B)

        difference = counterA.keys()^counterB.keys()

        for i in difference:
            if(i in counterA):
                if(counterA[i] == 1):
                    uncommon.append(i)
            if(i in counterB):
                if(counterB[i] == 1):
                    uncommon.append(i)

        return(uncommon)