class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff

            # If tank becomes negative,
            # current start is not possible
            if tank < 0:
                start = i + 1
                tank = 0

        # If total gas < total cost, impossible
        return start if total >= 0 else -1
        