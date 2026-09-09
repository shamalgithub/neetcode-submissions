class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for sub_array in matrix:
            left_p = 0 
            right_p = len(sub_array) - 1 

            while left_p <= right_p : 

                mid_point = (left_p + right_p) // 2 
                if sub_array[mid_point] == target:
                    return True 
                
                elif sub_array[mid_point] < target: 
                    left_p = mid_point + 1 
                
                elif sub_array[mid_point] > target : 
                    right_p = mid_point - 1 
            
        return False 
        