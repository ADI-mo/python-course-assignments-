import math
from typing import List, Tuple
# Import the required function from SciPy for linear regression
from scipy.stats import linregress
import numpy as np

def growth_rate(N_t: float, N_0: float, t: float) -> float:
    """
    Calculates the Specific Growth Rate (k) based on two time points.

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
    # n = log2(N_t / N_0)
    num_generations = math.log2(N_t) - math.log2(N_0)

    # Calculate the specific growth rate (k = n/t).
    k = num_generations / t

    return k

def growth_rate_fit(time_points: List[float], concentration_points: List[float]) -> Tuple[float, float]:
    """
    Calculates the Specific Growth Rate (k) by linear regression (SciPy)
    using multiple time and concentration points.

    It fits a line to the log2-transformed concentration data over time:
    log2(Concentration) = k * Time + intercept

    Args:
        time_points (List[float]): List of time measurements. Must be non-decreasing.
        concentration_points (List[float]): List of corresponding concentration measurements (must be > 0).

    Returns:
        Tuple[float, float]: (Specific Growth Rate (k), R-squared value of the fit).

    Raises:
        ValueError: If lists are empty, have different lengths, or contain non-positive values.
    """
    if len(time_points) < 2 or len(concentration_points) < 2:
        raise ValueError("Error: At least two data points (time and concentration) are required for fitting.")
    if len(time_points) != len(concentration_points):
        raise ValueError("Error: Time and concentration lists must have the same length.")

    # Convert to NumPy arrays for SciPy and perform log transformation
    time_array = np.array(time_points)
    concentration_array = np.array(concentration_points)

    if (time_array <= 0).any() and time_points[0] != 0:
         raise ValueError("Error: All time points must be positive (unless the first is 0).")
    if (concentration_array <= 0).any():
        raise ValueError("Error: All concentration points must be positive.")

    # Calculate log2 of concentration
    log2_concentration = np.log2(concentration_array)

    # Perform linear regression: slope is the growth rate (k)
    # The result object contains slope, intercept, r-value, p-value, and stderr
    slope, intercept, r_value, p_value, std_err = linregress(time_array, log2_concentration)

    # R-squared value is r_value squared
    r_squared = r_value ** 2

    # The slope 'slope' directly represents the growth rate k (generations/time)
    k = slope

    return k, r_squared

# Example usage (for reference, but typically used via the GUI/CLI)
if __name__ == "__main__":
    # Single point calculation
    k_single = growth_rate(100000.0, 1000.0, 5.0)
    print(f"Single point Growth Rate (k): {k_single:.4f} gen/time")

    # Multi-point calculation
    times = [0, 1, 2, 3, 4, 5]
    concentrations = [1000, 2000, 4000, 8000, 16000, 32000] # Perfect doubling every hour (k=1)
    k_multi, r2 = growth_rate_fit(times, concentrations)
    print(f"Multi-point Growth Rate (k): {k_multi:.4f} gen/time (R-squared: {r2:.4f})")