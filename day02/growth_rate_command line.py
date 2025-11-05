import math
import sys

# -------------------------------------------------------------
# פונקציה לחישוב קצב הגידול (Growth_rate) - נשארת זהה
def growth_rate(N_t, N_0, t):
    """
    Calculate the Specific Growth Rate (k) of a cell/Bacteria.
    Formula: k = (log2(N_t) - log2(N_0)) / t 
    """
    if t <= 0 or N_t <= 0 or N_0 <= 0:
        raise ValueError("Error: All parameters (N_t, N_0, t) must be positive.")
        
    num_generations = math.log2(N_t) - math.log2(N_0)
    k = num_generations / t
    return k

# -------------------------------------------------------------
# הפונקציה המבצעת את החישוב בממשק CLI
def cli_growth_rate_calculator():
    
    # 1. בדיקת מספר הארגומנטים
    # sys.argv מכיל את שם הקובץ (אינדקס 0) ואחריו הארגומנטים. 
    # אנחנו צריכים 3 ארגומנטים נוספים (N_t, N_0, t), כלומר סה"כ 4 פריטים.
    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments.")
        print("Usage: python your_script_name.py <N_t> <N_0> <t>")
        print("Example: python calculator.py 100000 1000 5")
        sys.exit(1) # יציאה עם קוד שגיאה
    
    try:
        # 2. קבלת הקלט כארגומנטים בשורת הפקודה והמרה ל-float
        # sys.argv[1] הוא N_t, sys.argv[2] הוא N_0, sys.argv[3] הוא t
        N_t = float(sys.argv[1])
        N_0 = float(sys.argv[2])
        t = float(sys.argv[3])

        # 3. ביצוע החישוב
        k = growth_rate(N_t, N_0, t)
        
        # 4. הדפסת התוצאה
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
        # לכידת שגיאות מהפונקציה growth_rate (כמו קלט שלילי)
        print(f"\nAn error occurred: {e}")
        sys.exit(1)

# הפעלת התוכנית ב-CLI
if __name__ == "__main__":
    cli_growth_rate_calculator()