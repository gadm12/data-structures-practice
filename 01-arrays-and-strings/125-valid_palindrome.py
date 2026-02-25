class Solution:
    """
    Valid Palindrome
    Cleans the string of non-alphanumeric characters and compares to its reverse.
        - Time Complexity: O(n)
        - Space Complexity: O(n) to store the cleaned string.
    """

    def is_palindrome(self, s: str) -> bool:

        cleaned = "".join(char.lower() for char in s if char.isalnum())

        cleaned == cleaned[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.is_palindrome("A man, a plan, a canal: Panama"))
    print(sol.is_palindrome("race a car"))
