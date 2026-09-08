class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        start, end = newInterval

        for s, e in intervals:
            if e < start:
                result.append([s, e])
            elif end < s:
                result.append([start, end])
                start, end = s, e
            else:
                start = min(s, start)
                end = max(e, end)
        result.append([start, end])
        return result

        