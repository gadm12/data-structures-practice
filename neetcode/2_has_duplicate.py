class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        set_nums = set(nums)

        if len(nums) > len(set_nums):
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate(1, 2, 3, 3))
