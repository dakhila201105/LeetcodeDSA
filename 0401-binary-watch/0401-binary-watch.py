class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        # The values corresponding to each of the 10 LED positions
        # First 4 are hours (8, 4, 2, 1), next 6 are minutes (32, 16, 8, 4, 2, 1)
        led_values = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        result = []
        
        def backtrack(index: int, total_on: int, hours: int, minutes: int):
            # Pruning conditions for invalid clock times
            if hours >= 12 or minutes >= 60:
                return
            
            # Base case: if we have turned on the required number of LEDs
            if total_on == turnedOn:
                result.append(f"{hours}:{minutes:02d}")
                return
            
            # If we out of LEDs to check or have chosen too many
            if index >= len(led_values):
                return
                
            # Choice 1: Turn ON the current LED at 'index'
            if index < 4:
                backtrack(index + 1, total_on + 1, hours + led_values[index], minutes)
            else:
                backtrack(index + 1, total_on + 1, hours, minutes + led_values[index])
                
            # Choice 2: Leave the current LED OFF
            backtrack(index + 1, total_on, hours, minutes)

        backtrack(0, 0, 0, 0)
        return result
