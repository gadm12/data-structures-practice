class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 2, 4, 6, 8], 4))
    print(sol.search([-1, 0, 2, 4, 6, 8], 4))