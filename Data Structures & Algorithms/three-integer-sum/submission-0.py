class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, i in enumerate(nums):
            if index > 0 and i == nums[index - 1]:
                continue
            if i > 0:
                break  # optimization: if smallest remaining is already positive, no triplet can sum to 0

            l, r = index + 1, len(nums) - 1
            while l < r:
                threesum = i + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    result.append([i, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return result

                
        