class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        warmer_days = [0 for i in range(len(temperatures))]

        for index , t in enumerate(temperatures): 

            # we add temperatures to the stack if the values in the stack are greater than 
            # current temperature t , else we pop the values until the remainder is greater 
            while stack and t > temperatures[stack[-1]]:
                prev_index = stack.pop()
                warmer_days[prev_index] = index - prev_index 
            stack.append(index)

        return warmer_days 










        