class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # cant assume its sorted 
        # create a hashmap 

        preMap = {} # val : index 

        for index , i in enumerate(nums):
            difference = target - i 
            if difference in preMap: 
                return [preMap[difference] , index]
            else:
                preMap[i] = index 
            