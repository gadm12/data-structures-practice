class Solution:
    """
    Contains Duplicate
    Check if any value appears more than once in the array.
    Uses a set to track seen value.
        -Time Complexity: O(n) - Single pass through the array
        -Space Complexity: O(n) - Set stores up to n element in the worst case
    Trade-off: We use extra memory to avoid a brute force O(n^2) nested loop comparison.
    """

    def contains_duplicate(self, nums):
        seen = set()

        for num in nums:

            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.contains_duplicate([1, 2, 3, 1]))
    print(sol.contains_duplicate([1, 2, 3, 4]))
    print(sol.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
