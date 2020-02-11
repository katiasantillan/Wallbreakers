class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums = list(enumerate(nums, start = 0))
        nums.sort(key = lambda x:x[1])
        
        left = 0
        right = len(nums)-1
        
        while(left < right):
            
            suma = nums[left][1] + nums[right][1]
            
            if(suma == target):
                return([nums[left][0], nums[right][0]])
            elif(suma > target):
                right -= 1
            elif(suma < target):
                left +=1
            
        