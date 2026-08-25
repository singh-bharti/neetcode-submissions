class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        subset = []
        mapTable = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz'
        }
        def dfs(index):
            if index == len(digits):
                result.append("".join(subset))
                return

            digit = digits[index]

            for letter in mapTable[digit]:
                subset.append(letter)

                dfs(index + 1)

                subset.pop()
        dfs(0)
        return result

