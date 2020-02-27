class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binSearch(nums, lL, lR, target):
            if(lR>=lL):
                mid = lL+(lR-lL)//2

                if(nums[mid] == target):
                    return mid
                elif(nums[mid] > target):
                    return binSearch(nums, lL, mid-1, target)
                else:
                    return binSearch(nums, mid+1, lR, target)

            else:
                return -1
        
        return(binSearch(nums, 0, len(nums)-1, target))