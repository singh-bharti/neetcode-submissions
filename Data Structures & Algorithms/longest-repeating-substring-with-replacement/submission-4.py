class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            count = {}
            l = 0
            maxF = 0
            result = 0
            for r in range(len(s)):
                count[s[r]] = count.get(s[r], 0) + 1

                maxF = max(maxF, count[s[r]])

                while (r - l + 1) - maxF > k:
                    count[s[l]] -= 1
                    l += 1
                
                result = max(result, r - l + 1)
            return result
        