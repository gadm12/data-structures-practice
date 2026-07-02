class Solution:
    def sort_sentence(self, s: str) -> str:
        # s = s.split()
        # sorted_lst = sorted(s, key=lambda i: i[-1], reverse=False)
        # words = []
        # for word in sorted_lst:
        #     words.append(word[:-1])

        # return " ".join(words)
        return " ".join([word[:-1] for word in sorted(s.split(), key=lambda i: i[-1], reverse=False)])
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.sort_sentence("is2 sentence4 This1 a3"))