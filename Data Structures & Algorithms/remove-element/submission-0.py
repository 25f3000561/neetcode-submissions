class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count_val=nums.count(val)
        while val in nums:
            nums.remove(val)
                
        return(len(nums))