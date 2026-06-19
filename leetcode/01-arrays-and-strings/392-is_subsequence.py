class Solution:
    """
    Is Subsequence
    Uses a two-pointer approach to scan 't' for characters in 's' while maintaining order.
        - Time Complexity: O(n), where n is the length of string 't'.
        - Space Complexity: O(1), as it only uses two integer pointers.
    """

    def is_subsequence(self, s: str, t: str) -> bool:

        s_ptr, t_ptr = 0, 0

        while s_ptr < len(s) and t_ptr < len(t):

            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1

            t_ptr += 1

        return s_ptr == len(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.is_subsequence("abc", "ahbgdc"))
    print(sol.is_subsequence("axc", "ahbgdc"))
