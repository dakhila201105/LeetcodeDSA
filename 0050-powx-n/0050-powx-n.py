class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: any number to the power of 0 is 1
        if n == 0:
            return 1.0
        
        # Handle negative exponents
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1.0
        current_product = x
        
        # Iterative Binary Exponentiation
        while n > 0:
            # If the current bit of n is 1, multiply the result by current_product
            if n % 2 == 1:
                res *= current_product
                
            # Square the base product and shift n down by half
            current_product *= current_product
            n //= 2
            
        return res
