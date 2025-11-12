import pytest
from Growth_Rate_Logic_and_SciPy_Fit import growth_rate, growth_rate_fit
import numpy as np

# --- Tests for the single-point growth_rate function ---

def test_growth_rate_perfect_doubling():
    """Test case for perfect doubling in one unit of time (k should be 1.0)."""
    # N_t = 2 * N_0, t = 1.0
    k = growth_rate(N_t=100.0, N_0=50.0, t=1.0)
    assert k == 1.0

def test_growth_rate_ten_doublings_in_five_hours():
    """Test case for 10 doublings (1024-fold increase) in 5 hours (k should be 2.0)."""
    # N_t = 1024 * N_0 (2^10), t = 5.0. k = 10/5 = 2.0
    k = growth_rate(N_t=10240.0, N_0=10.0, t=5.0)
    assert k == 2.0

def test_growth_rate_no_growth():
    """Test case where N_t equals N_0 (k should be 0.0)."""
    k = growth_rate(N_t=75.0, N_0=75.0, t=3.0)
    assert k == 0.0

def test_growth_rate_negative_t_raises_value_error():
    """Test that non-positive time raises ValueError."""
    with pytest.raises(ValueError, match="All parameters.*must be positive"):
        growth_rate(N_t=100.0, N_0=50.0, t=-1.0)

def test_growth_rate_zero_n0_raises_value_error():
    """Test that non-positive initial concentration raises ValueError."""
    with pytest.raises(ValueError, match="All parameters.*must be positive"):
        growth_rate(N_t=100.0, N_0=0.0, t=5.0)

def test_growth_rate_negative_nt_raises_value_error():
    """Test that non-positive final concentration raises ValueError."""
    with pytest.raises(ValueError, match="All parameters.*must be positive"):
        growth_rate(N_t=-100.0, N_0=50.0, t=5.0)

# --- Tests for the multi-point growth_rate_fit function (SciPy) ---

def test_growth_rate_fit_perfect_data_k1():
    """Test perfect linear data where k should be 1.0."""
    # Doubling every time unit: [1, 2, 4, 8, 16] -> log2 is [0, 1, 2, 3, 4]
    times = [0, 1, 2, 3, 4]
    concentrations = [1.0, 2.0, 4.0, 8.0, 16.0]
    k, r2 = growth_rate_fit(times, concentrations)
    # Check if k is close to 1.0 and R-squared is 1.0
    assert np.isclose(k, 1.0)
    assert np.isclose(r2, 1.0)

def test_growth_rate_fit_stagnant_data_k0():
    """Test stagnant data where k should be 0.0."""
    times = [0, 1, 2, 3, 4]
    concentrations = [5.0, 5.0, 5.0, 5.0, 5.0]
    k, r2 = growth_rate_fit(times, concentrations)
    # Check if k is close to 0.0 and R-squared is 1.0
    assert np.isclose(k, 0.0)
    assert np.isclose(r2, 1.0)

def test_growth_rate_fit_real_world_data():
    """Test data with slight noise, k should be approximately 0.5."""
    # Data that roughly doubles every 2 hours (k=0.5)
    times = [0.0, 1.0, 2.0, 3.0, 4.0]
    concentrations = [10.0, 14.5, 21.0, 30.0, 43.0]
    k, r2 = growth_rate_fit(times, concentrations)
    # k is roughly 0.54, R2 is high
    assert 0.5 < k < 0.6
    assert r2 > 0.99

def test_growth_rate_fit_not_enough_points():
    """Test that less than two points raises ValueError."""
    with pytest.raises(ValueError, match="At least two data points"):
        growth_rate_fit(time_points=[1.0], concentration_points=[10.0])

def test_growth_rate_fit_mismatched_lengths():
    """Test that lists of different lengths raise ValueError."""
    with pytest.raises(ValueError, match="Time and concentration lists must have the same length"):
        growth_rate_fit(time_points=[1.0, 2.0], concentration_points=[10.0])

def test_growth_rate_fit_non_positive_concentration():
    """Test that non-positive concentrations raise ValueError."""
    times = [0, 1, 2]
    concentrations = [1.0, 2.0, -4.0] # Negative concentration
    with pytest.raises(ValueError, match="All concentration points must be positive"):
        growth_rate_fit(times, concentrations)