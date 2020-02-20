class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        numCandies = len(candies)//2

        candiesC = set(candies)

        if (len(candiesC) >= numCandies):
            return(numCandies)
        else:
            return(len(candiesC))