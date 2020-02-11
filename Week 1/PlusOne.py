class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        i = len(digits)-1
        op = digits[i]+1
        
        if (op == 10):
            carry = 1
            
            while(carry):
                digits[i] = 0
                i -= 1
                
                if(i<0):
                    digits.insert(0, 1)
                    carry = 0
                else:
                    op = digits[i]+1
                    
                    if(op != 10):
                        digits[i] = op
                        carry = 0
        else:
            digits[-1] = op
        
        return digits