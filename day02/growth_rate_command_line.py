import math
import sys
from calculator_logic import growth_rate


# -------------------------------------------------------------
# Command-Line Interface (CLI) function
def cli_growth_rate_calculator():
    # 1. Validating the number of command-line arguments
    # sys.argv[0]is the name of the file itself
    # we expect three additional arguments: N_t, N_0, and t
    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments.")
        print("Usage: python your_script_name.py <N_t> <N_0> <t>")
        print("Example: python calculator.py 100000 1000 5")
        sys.exit(1) # Exit with error code
    
    try:
        # 2. Parsing the command-line arguments
        # Convert the arguments from strings to floats
        N_t = float(sys.argv[1])
        N_0 = float(sys.argv[2])
        t = float(sys.argv[3])

        # 3.Performing the calculation
        k = growth_rate(N_t, N_0, t)
        
        # 4. Printing the result
        print(f"\n--- Growth Rate Calculation (CLI) ---")
        print(f"N_t (Final Density): {N_t}")
        print(f"N_0 (Initial Density): {N_0}")
        print(f"t (Time Interval): {t}")
        print(f"The specific growth rate (k) is: {k:.4f} generations per unit time.")
        
    except ValueError:
        print("\nError: All arguments must be valid positive numbers.")
        print("Usage: python your_script_name.py <N_t> <N_0> <t>")
        sys.exit(1)
        
    except Exception as e:
        # Catch-all for any other exceptions
        print(f"\nAn error occurred: {e}")
        sys.exit(1)

#Running the program in the CLI
if __name__ == "__main__":
    cli_growth_rate_calculator()