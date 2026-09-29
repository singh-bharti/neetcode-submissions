class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            totalGas += diff
            tank += diff 

            if tank < 0:
                start = i + 1
                tank = 0
        if totalGas < 0:
            return -1
        return start
        