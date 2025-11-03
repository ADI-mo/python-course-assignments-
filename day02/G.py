
import math
def Growth_rate(N_t, N_0,t):
    """
    Calculate the Growth_rate of a cell/Bacteria.
    
    Formula: k= (log(N_t)-log(N_0))/(log(2)*t) 
    
    Args:
        N_t (float): Population density at finite time (t)
        N_0 (float):Population density at initial time (t=0)
        t (float): time interval
    Returns:
        float:  The Growth_rate of the cell/Bacteria    
    """
    Growth_rate =((math.log2(N_t)-math.log2(N_0))/t)
    return Growth_rate

import math

# הפונקציה לחישוב קצב הגידול (ללא שינוי, היא תקינה)
def Growth_rate(N_t, N_0,t):
    if t <= 0 or N_t <= 0 or N_0 <= 0:
        # מאחדים את כל בדיקות הקלט השלילי/אפסי לשורה אחת
        raise ValueError("Error: All parameters (N_t, N_0, t) must be positive.")
        
    num_generations = math.log2(N_t) - math.log2(N_0)
    k = num_generations / t
    return k

# -------------------------------------------------------------
# פונקציית עזר פשוטה לקבלת קלט חיובי
def get_positive_float(prompt_text):
"Prompts input from the user in a loop until a positive number is received." 
while True:
        try:
            value_str = input(prompt_text)
            num = float(value_str)
            
            if num > 0:
                return num  # יציאה מהפונקציה והחזרת הערך
            else:
                print("הערך חייב להיות גדול מאפס. נסה שוב.")
        except ValueError:
            print("קלט לא תקין. אנא הזן מספר חוקי.")

# -------------------------------------------------------------
# הפונקציה האינטראקטיבית המפושטת
def interactive_growth_rate_calculator_simple():
    print("--- מחשבון אינטראקטיבי לקצב גידול (k) ---")

    # קריאה לפונקציית העזר לקבלת כל אחד מהפרמטרים
    try:
        N_t = get_positive_float("צפיפות סופית (N_t): ")
        N_0 = get_positive_float("צפיפות התחלתית (N_0): ")
        t = get_positive_float("מרווח זמן (t): ")

        # ביצוע החישוב
        k = growth_rate(N_t, N_0, t)
        
        print("\n--- תוצאה ---")
        print(f"קצב הגידול (k) הוא: {k:.4f} דורות ליחידת זמן.")
        
    except Exception as e:
        # יטפל בשגיאות אם קיימות (בעיקר אם קוד ה-growth_rate משתנה)
        print(f"\nאירעה שגיאה: {e}")

# הפעלת התוכנית האינטראקטיבית
if __name__ == "__main__":
    interactive_growth_rate_calculator_simple()

  