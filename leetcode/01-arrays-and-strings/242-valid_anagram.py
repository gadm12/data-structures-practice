class Solution:
    """
    Valid Anagram
    Determines if string 't' is a rearrangement of string 's'.
    Uses a frequency map (dictionary) to count character occurrences.
        - Time Complexity: O(n) where n is the length of the strings.
        - Space Complexity: O(k) where k is the number of unique characters (or O(1) if limited to a fixed alphabet like lowercase a-z).
    Trade-off: Uses a hash map to achieve linear time, avoiding the O(n log n) cost of sorting.
    """

    def is_anagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.is_anagram("anagram", "nagaram"))
    print(sol.is_anagram("rat", "car"))
