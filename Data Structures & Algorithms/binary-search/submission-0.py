class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_p = 0 
        right_p = len(nums) - 1 

        while left_p <= right_p : 

            midway_point = (left_p + right_p) // 2

            if nums[midway_point] == target: 
                return midway_point 
            elif nums[midway_point] > target:
                right_p = midway_point - 1 
            elif nums[midway_point] < target:
                left_p = midway_point + 1 
            
        return -1 
        