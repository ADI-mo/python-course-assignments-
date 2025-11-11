import math
import tkinter as tk
from tkinter import messagebox # Module for pop-up messages
from calculator_logic import growth_rate # Assuming 'calculator_logic.py' exists


# -------------------------------------------------------------
#Core function linked to the button
def calculate_growth_rate_gui():
    try:
        # 1. Capture input from the GUI elements and convert to float
        N_t = float(entry_Nt.get())
        N_0 = float(entry_N0.get())
        t = float(entry_t.get())
        unit_time = time_unit_var.get()
        # 2. Perform the calculation (The function will raise ValueError if input is negative/zero)
        k = growth_rate(N_t, N_0, t)
        
        # 3. Display the result in the GUI
       result_label.config(text=f"Growth Rate (k): {k:.4f} gen/{unit_time}", fg="purple")     
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
        result_label.config(text="Calculation Failed", fg="red")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        result_label.config(text="Calculation Failed", fg="red")

# -------------------------------------------------------------
# Defining the Graphical User Interface (GUI)
# Create the main window
root = tk.Tk()
root.title("Microbial Growth Rate Calculator (k)")
time_unit_var = tk.StringVar(value="hours") # New variable to hold time unit
# Define input fields and labels using grid layout for clean organization
# N_t (Final Density)
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

# Time Unit Input Field (This section must be MOVED UP and enabled)
tk.Label(root, text="Time Unit:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
# FIX 2: ENABLE AND USE THE DEFINED time_unit_var
entry_time_unit = tk.Entry(root, textvariable=time_unit_var) 
entry_time_unit.grid(row=3, column=1, padx=5, pady=5)

# Button to trigger calculation
calculate_button = tk.Button(root, text="Calculate Growth Rate (k)", command=calculate_growth_rate_gui)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Enter values and click Calculate.", font=('Arial', 10, 'bold'))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the GUI event loop (MUST BE THE LAST LINE OF THE SETUP)
root.mainloop()