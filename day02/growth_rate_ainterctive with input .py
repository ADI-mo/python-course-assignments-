import math

# -------------------------------------------------------------
# פונקציה לחישוב קצב הגידול (Growth_rate)
# שמה שונה ל-growth_rate (snake_case)
def growth_rate(N_t, N_0, t):
    """
    Calculate the Specific Growth Rate (k) of a cell/Bacteria.
    
    Formula: k = (log2(N_t) - log2(N_0)) / t 
    
    Args:
        N_t (float): Population density at finite time (t)
        N_0 (float): Population density at initial time (t=0)
        t (float): time interval
    Returns:
        float: The Specific Growth Rate (k) in units of generations/time. 
    """
    # בדיקת קלט מאוחדת: כל הפרמטרים חייבים להיות חיוביים.
    if t <= 0 or N_t <= 0 or N_0 <= 0:
        raise ValueError("Error: All parameters (N_t, N_0, t) must be positive.")
        
    num_generations = math.log2(N_t) - math.log2(N_0)
    k = num_generations / t
    return k

# -------------------------------------------------------------
# פונקציית עזר פשוטה לקבלת קלט חיובי
def get_positive_float(prompt_text):
    """Prompts input from the user in a loop until a positive number is received.""" 
    while True:
        try:
            value_str = input(prompt_text)
            num = float(value_str)
            
            if num > 0:
                return num  # יציאה מהפונקציה והחזרת הערך
            else:
                print('Value must be greater than zero. Try again.')
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# -------------------------------------------------------------
# הפונקציה האינטראקטיבית המפושטת
def interactive_growth_rate_calculator_simple():
    print("--- Interactive growth rate calculator (k) ---")

    try:
        # קריאה לפונקציית העזר לקבלת כל אחד מהפרמטרים
        N_t = get_positive_float("Population density at finite time (N_t): ")
        N_0 = get_positive_float("Population density at initial time (N_0): ")
        t = get_positive_float("Time interval (t): ")

        # ביצוע החישוב (שימוש בשם המתוקן: growth_rate)
        k = growth_rate(N_t, N_0, t)
        
        print("\n--- Result ---")
        print(f"The growth rate (k) is: {k:.4f} generations per unit time.")
        
    except Exception as e:
        # טיפול בשגיאות
        print(f"\nAn error occurred: {e}")

# הפעלת התוכנית האינטראקטיבית
if __name__ == "__main__":
    interactive_growth_rate_calculator_simple()