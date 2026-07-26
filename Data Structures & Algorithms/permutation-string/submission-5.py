class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_count = {}
        window_count = {}

        for ch in s1:
            s1_count[ch] = 1 + s1_count.get(ch, 0)
        l = 0 
        for r in range(len(s2)):
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1

            if (r - l + 1) > len(s1):
                window_count[s2[l]] -= 1

                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]

                l += 1
            if window_count == s1_count: return True
        return False