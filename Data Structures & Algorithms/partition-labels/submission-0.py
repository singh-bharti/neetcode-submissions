class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, char in enumerate(s):
            last[char] = i
        result = []

        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last[char])
            # We can safely end this partition
            if i == end:
                result.append(i - start + 1)
                start = i + 1

        return result
            