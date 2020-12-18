class Solution:
    def sortedSquares(self, nums):
        out = [num**2 for num in nums]
        print(sorted(out))

nums = [-4,-1,0,3,10]
s = Solution()
s.sortedSquares(nums)