import math
from typing import List, Tuple
# Import the required function from SciPy for linear regression
from scipy.stats import linregress
import numpy as np

def growth_rate(N_t: float, N_0: float, t: float) -> float:
    """
    Calculates the Specific Growth Rate (k) of a cell or bacterial population
    based on two data points (N_0 and N_t) over a time interval (t).
    
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

def growth_rate_fit(time_points: List[float], concentration_points: List[float]) -> Tuple[float, float]:
    """
    Calculates the Specific Growth Rate (k) by performing linear regression on
    multiple time and concentration points using SciPy.
    
    The fit is performed on log2(N) vs Time (t), where k is the slope.
    
    Args:
        time_points (List[float]): List of time measurements.
        concentration_points (List[float]): List of concentration (N) measurements.
    
    Returns:
        Tuple[float, float]: (Specific Growth Rate (k), R-squared value of the fit).
        
    Raises:
        ValueError: If input lists are invalid (length, non-positive values).
    """
    
    # 1. Validation checks
    if len(time_points) != len(concentration_points):
        raise ValueError("Time and concentration lists must have the same length.")
    
    if len(time_points) < 2:
        raise ValueError("At least two data points are required for linear regression.")

    if any(c <= 0 for c in concentration_points):
        raise ValueError("All concentration points must be positive (>0) for log transformation.")
        
    # 2. Transform concentration data: log2(N)
    log2_concentrations = np.log2(concentration_points)
    
    # 3. Perform Linear Regression (SciPy)
    # The slope of log2(N) vs t is the growth rate (k)
    # r_value is the Pearson correlation coefficient
    slope, intercept, r_value, p_value, std_err = linregress(time_points, log2_concentrations)
    
    # The growth rate k is the slope
    k = slope
    
    # R-squared is the square of the Pearson correlation coefficient
    r_squared = r_value**2
    
    return k, r_squared

# This file does not run independently, it is imported by others.