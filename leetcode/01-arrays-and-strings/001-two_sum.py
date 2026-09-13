class Solution:
    

    def two_sum_1(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    

    def two_sum_2(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.two_sum_1([2, 7, 11, 15], 9))
    print(sol.two_sum_2([2, 7, 11, 15], 9))
