class CountSquares:

    def __init__(self):
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] = self.points.get((x, y), 0) + 1
        

    def count(self, point: List[int]) -> int:
        x, y = point

        result = 0

        for (x2, y2), count in self.points.items():
            if x2 == x or y2 == y:
                continue
            if abs(x2 - x) != abs(y2 - y):
                continue

            count1 = self.points.get((x, y2), 0) 
            count2 = self.points.get((x2, y), 0)

            result += count * count1 * count2
        return result
        
