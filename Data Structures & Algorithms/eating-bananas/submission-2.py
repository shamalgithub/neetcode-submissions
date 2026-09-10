class Solution:

    # could not solve - try again !!! 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_p = 1
        right_p = max(piles)
        result = right_p

        while left_p <= right_p:
            mid_point = (left_p + right_p) // 2
            hours = sum(math.ceil(p / mid_point) for p in piles)

            if hours <= h:
                result = mid_point
                right_p = mid_point - 1
            else:
                left_p = mid_point + 1

        return result
            
             






        