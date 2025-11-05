import math
import tkinter as tk
from tkinter import messagebox # מודול להצגת הודעות קופצות

# הפונקציה לחישוב קצב הגידול (כפי שתוקנה)
def growth_rate(N_t, N_0, t):
    if t <= 0 or N_t <= 0 or N_0 <= 0:
        # במקום להדפיס, נזרוק שגיאה שתטופל ב-GUI
        raise ValueError("All parameters (N_t, N_0, t) must be positive.")
    
    num_generations = math.log2(N_t) - math.log2(N_0)
    k = num_generations / t
    return k

# -------------------------------------------------------------
# פונקציית הליבה המקושרת לכפתור
def calculate_growth_rate_gui():
    try:
        # 1. לכידת קלט מהרכיבים והמרה ל-float
        N_t = float(entry_Nt.get())
        N_0 = float(entry_N0.get())
        t = float(entry_t.get())
        
        # 2. ביצוע החישוב (הפונקציה תזרוק ValueError אם הקלט שלילי/אפסי)
        k = growth_rate(N_t, N_0, t)
        
        # 3. הצגת התוצאה
        result_label.config(text=f"Growth Rate (k): {k:.4f} gen/time", fg="purple")
        
    except ValueError as e:
        # טיפול בשגיאות (כגון קלט שאינו מספר או מספר שאינו חיובי)
        # הצגת הודעה קופצת למשתמש במקום הדפסה לקונסול
        messagebox.showerror("Input Error", str(e))
        result_label.config(text="Calculation Failed", fg="pink")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        result_label.config(text="Calculation Failed", fg="red")

# -------------------------------------------------------------
# הגדרת ממשק המשתמש הגרפי (GUI)

# יצירת החלון הראשי
root = tk.Tk()
root.title("Microbial Growth Rate Calculator (k)")

# הגדרת שדות הקלט והתוויות באמצעות grid (רשת) לארגון נקי

# N_t (צפיפות סופית)
tk.Label(root, text="Final Density (N_t):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_Nt = tk.Entry(root)
entry_Nt.grid(row=0, column=1, padx=5, pady=5)

# N_0 (צפיפות התחלתית)
tk.Label(root, text="Initial Density (N_0):").grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_N0 = tk.Entry(root)
entry_N0.grid(row=1, column=1, padx=5, pady=5)

# t (מרווח זמן)
tk.Label(root, text="Time Interval (t):").grid(row=2, column=0, padx=5, pady=5, sticky='w')
entry_t = tk.Entry(root)
entry_t.grid(row=2, column=1, padx=5, pady=5)

# כפתור החישוב
calculate_button = tk.Button(root, text="Calculate Growth Rate (k)", command=calculate_growth_rate_gui)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# תווית להצגת התוצאה
result_label = tk.Label(root, text="Enter values and click Calculate.", font=('Arial', 10, 'bold'))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# הפעלת לולאת האירועים (הכרחי לכל יישום GUI)
root.mainloop()