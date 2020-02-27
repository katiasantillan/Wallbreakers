class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minV = float('inf')
        maxProfit = 0
        i = 0
        
        while(i<len(prices)):
            if(prices[i] < minV):
                minV = prices[i]
            
            if (prices[i] - minV) > maxProfit:
                maxProfit = prices[i] - minV
            
            i+=1
        
        return(maxProfit)