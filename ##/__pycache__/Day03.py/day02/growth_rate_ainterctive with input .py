import math

# -------------------------------------------------------------
# 
from calculator_logic import growth_rate # Assuming 'calculator_logic.py' exists


# -------------------------------------------------------------
#Helper function to receive positive input from the user
def get_positive_float(prompt_text):
    """Prompts input from the user in a loop until a positive number is received.""" 
    while True:
        try:
            value_str = input(prompt_text)
            num = float(value_str)
            
            if num > 0:
                return num  # Return the valid positive number
            else:
                print('Value must be greater than zero. Try again.')
        except ValueError:
            print("Invalid input. Please enter a valid number.")
#Helper function to get time unit from the user
def get_time_unit():
    """Prompts the user to enter a time unit for the growth rate."""
    time_unit = input("Enter the time unit for growth rate (e.g., hours, days): ")
    return time_unit.strip()  # Remove any leading/trailing whitespace

# -------------------------------------------------------------
# Core interactive function
def interactive_growth_rate_calculator_simple():
    print("--- Interactive growth rate calculator (k) ---")

    try:
        # Capture user input
        N_t = get_positive_float("Population density at finite time (N_t): ")
        N_0 = get_positive_float("Population density at initial time (N_0): ")
        t = get_positive_float("Time interval (t): ")
        time_unit = get_time_unit() # NEW: Capture the time unit

        # Performing the calculation
        k = growth_rate(N_t, N_0, t)
        
        print("\n--- Result ---")
        # Display the result with the captured unit (MODIFIED)
        print(f"The growth rate (k) is: {k:.4f} generations per {time_unit}.")
        
    except Exception as e:
        # Catch any unexpected errors from growth_rate function
        print(f"\nAn error occurred: {e}")

#Running the interactive program
if __name__ == "__main__":
    interactive_growth_rate_calculator_simple()