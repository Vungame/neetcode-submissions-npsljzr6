class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations == 0:
            return init

        res = init
        for i in range(iterations):
            derOld = (2 * res)
            res -= learning_rate * derOld
        
        return round(res, 5)