import math

def growth_rate(N_t, N_0, t):
    """
    Calculates the Specific Growth Rate (k) of a cell or bacterial population.
    
    Formula: k = (log2(N_t) - log2(N_0)) / t 
    
    Args:
        N_t (float): Population density at finite time (t).
        N_0 (float): Population density at initial time (t=0).
        t (float): Time interval.
    
    Returns:
        float: The Specific Growth Rate (k) in units of generations/time. 
    
    Raises:
        ValueError: If any parameter (N_t, N_0, or t) is zero or negative.
    """
    # Unified input validation: All parameters must be positive.
    if t <= 0 or N_t <= 0 or N_0 <= 0:
        raise ValueError("Error: All parameters (N_t, N_0, t) must be positive.")
        
    # Calculate the number of generations (n) that occurred during time t.
    num_generations = math.log2(N_t) - math.log2(N_0)
    
    # Calculate the specific growth rate (k = n/t).
    k = num_generations / t
    
    return k

# Example usage:
# k_result = growth_rate(100000.0, 1000.0, 5.0)
# print(f"Growth Rate: {k_result}")