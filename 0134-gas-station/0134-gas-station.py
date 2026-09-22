class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # If the total fuel available is less than total required trip cost,
        # it is mathematically impossible to complete the circuit.
        if sum(gas) < sum(cost):
            return -1
            
        tt = 0
        sidx = 0
        
        for i in range(len(gas)):
            tt += gas[i] - cost[i]
            
            # If the fuel tank drops below zero, this starting position 
            # (and all intermediate stations visited so far) cannot be valid.
            if tt < 0:
                # Reset tank balance and try the next station as the candidate
                tt = 0
                sidx = i + 1
                
        return sidx