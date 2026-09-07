class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left , right = 0 , len(numbers) - 1 

        while left < right: 
            current_sum = numbers[left]+ numbers[right]
            if current_sum == target:
                return [left+1 , right+1]
            elif current_sum < target : # meaning we should move left 
                left += 1 
            else: # we should move away from the right 
                right -= 1 

            
        
        return [0 , 0]
            

        