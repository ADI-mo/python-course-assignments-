import math
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk # NEW: Import ttk for Combobox
from cGrowth Rate Logic and SciPy Fit  import growth_rate 


# -------------------------------------------------------------
# Core function linked to the button
def calculate_growth_rate_gui():
    try:
        # 1. Capture input from the GUI elements and convert to float
        N_t = float(entry_Nt.get())
        N_0 = float(entry_N0.get())
        t = float(entry_t.get())
        
        # Get the unit string from the globally defined variable (unchanged)
        unit_time = time_unit_var.get()
        
        # 2. Perform the calculation (The function will raise ValueError if input is negative/zero)
        k = growth_rate(N_t, N_0, t)
        
        # 3. Display the result in the GUI
        result_label.config(text=f"Growth Rate (k): {k:.4f} gen/{unit_time}", fg="purple")     
    except ValueError as e:
        # Handle errors
        messagebox.showerror("Input Error", str(e))
        result_label.config(text="Calculation Failed", fg="red")
    except Exception as e:
        # Handle unexpected errors
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        result_label.config(text="Calculation Failed", fg="red")

# -------------------------------------------------------------
# Defining the Graphical User Interface (GUI)

# Create the main window (FIRST STEP)
root = tk.Tk()
root.title("Microbial Growth Rate Calculator (k)")

# Define the list of allowed time units
ALLOWED_TIME_UNITS = ["hours", "minutes", "days", "seconds"] 

# FIX 1: Define tk.StringVar (must be after root)
time_unit_var = tk.StringVar(value=ALLOWED_TIME_UNITS[0]) # Default to the first unit

# Define input fields and labels using grid layout for clean organization
# N_t (Final Density)
tk.Label(root, text="Final Density (N_t, e.g. OD):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_Nt = tk.Entry(root)
entry_Nt.grid(row=0, column=1, padx=5, pady=5)

# N_0 (Initial Density)
tk.Label(root, text="Initial Density (N_0, e.g. OD):").grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_N0 = tk.Entry(root)
entry_N0.grid(row=1, column=1, padx=5, pady=5)

# t (Time Interval)
tk.Label(root, text="Time Interval (t):").grid(row=2, column=0, padx=5, pady=5, sticky='w')
entry_t = tk.Entry(root)
entry_t.grid(row=2, column=1, padx=5, pady=5)

# FIX 2: REPLACE Entry with Combobox
tk.Label(root, text="Time Unit:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
entry_time_unit = ttk.Combobox(
    root,
    textvariable=time_unit_var,
    values=ALLOWED_TIME_UNITS, # Restricts input to this list
    state="readonly"           # Prevents typing in values not in the list
)
entry_time_unit.grid(row=3, column=1, padx=5, pady=5)


# Button to trigger calculation
calculate_button = tk.Button(root, text="Calculate Growth Rate (k)", command=calculate_growth_rate_gui)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Enter values and click Calculate.", font=('Arial', 10, 'bold'))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()