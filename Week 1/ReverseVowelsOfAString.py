class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        sNew = list(s)
        
        newOrder = []
        for i in sNew:
            if i in vowels:
                newOrder.append(i)
        
        
        for j in range(len(sNew)):
            if sNew[j] in vowels:
                sNew[j] = newOrder.pop()
        
        sNew = ("").join(sNew)
        return sNew