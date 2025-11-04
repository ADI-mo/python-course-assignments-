import math

# Function to calculate the growth rate
def growth_rate(N_t, N_0, t):
    """
    Calculate the Specific Growth Rate (k) of a cell/Bacteria.
    Formula: k = (log2(N_t) - log2(N_0)) / t 
    """
    # Consolidated input validation
    if t <= 0 or N_t <= 0 or N_0 <= 0:
        raise ValueError("Error: All parameters (N_t, N_0, t) must be positive.")
        
    num_generations = math.log2(N_t) - math.log2(N_0)
    k = num_generations / t
    return k

# -------------------------------------------------------------
# Helper function to get valid positive floating-point input
def get_positive_float(prompt_text):
    """Prompts input from the user in a loop until a positive number is received.""" 
    while True:
        try:
            value_str = input(prompt_text)
            num = float(value_str)
            
            if num > 0:
                return num 
            else:
                # English error message
                print('Value must be greater than zero. Try again.')
        except ValueError:
            # English error message
            print("Invalid input. Please enter a valid number.")

# -------------------------------------------------------------
# The simplified interactive function
def interactive_growth_rate_calculator_simple():
    # English title
    print("--- Interactive growth rate calculator (k) ---") 

    try:
        # English prompts for input
        N_t = get_positive_float("Enter Final Population Density (N_t): ")
        N_0 = get_positive_float("Enter Initial Population Density (N_0): ")
        t = get_positive_float("Enter Time interval (t): ")

        # Perform calculation
        k = growth_rate(N_t, N_0, t)
        
        # English result output
        print("\n--- Result ---")
        print(f"The growth rate (k) is: {k:.4f} generations per unit time.")
        
    except Exception as e:
        # English error handling
        print(f"\nAn error occurred: {e}")

# Run the interactive program
if __name__ == "__main__":
    interactive_growth_rate_calculator_simple()