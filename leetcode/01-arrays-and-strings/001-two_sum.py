class Solution:
    """
    The first solution to the Two Sum problem (brute force)
    Using a nested loops:
        -The outer loop runs n times
        -Redundant search: Each element is compared against every other element in the array.
    The time complexity of O(n^2)
    """

    def two_sum_1(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    """
    The second solution to the Two Sum problem
    Optimized approach using a Hash Map (Dictionary).
        - Time Complexity: O(n) - We only traverse the list once.
        - Space Complexity: O(n) - We store elements in a dictionary to allow O(1) lookups.
    Trade-off: We use more memory to achieve significantly faster speeds.
    """

    def two_sum_2(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            seen[num] = i
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.two_sum_1([2, 7, 11, 15], 9))
    print(sol.two_sum_2([2, 7, 11, 15], 9))
