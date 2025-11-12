import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import io

# Import the enhanced logic, including the SciPy fitting function
from Gcalculator_logic import growth_rate, growth_rate_fit

# --- Global Configuration and State ---
ALLOWED_TIME_UNITS = ["hours", "minutes", "days", "seconds"]
DATA_POINTS = [] # Global list to store (time, concentration) tuples

# --- Core Logic Functions ---

def update_data_table(tree_widget: ttk.Treeview):
    """Clears and repopulates the Treeview widget with current DATA_POINTS."""
    # Clear existing data
    for item in tree_widget.get_children():
        tree_widget.delete(item)
    # Insert new data
    for i, (t, c) in enumerate(DATA_POINTS):
        tree_widget.insert('', 'end', values=(i + 1, f"{t:.2f}", f"{c:.2f}"))

def add_data_point():
    """Captures and validates time and concentration inputs, then updates the table/plot."""
    try:
        t = float(entry_time_t.get())
        c = float(entry_conc_N.get())

        if t < 0 or c <= 0:
            raise ValueError("Time must be non-negative (>=0) and Concentration must be positive (>0).")

        DATA_POINTS.append((t, c))
        DATA_POINTS.sort(key=lambda x: x[0]) # Keep points sorted by time

        update_data_table(data_tree)
        # Clear inputs for the next entry
        entry_time_t.delete(0, tk.END)
        entry_conc_N.delete(0, tk.END)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def remove_data_point():
    """Removes the selected data point from the list."""
    selected_item = data_tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a data point to remove.")
        return

    # Get the row index (0-based) from the selected item
    row_id = data_tree.item(selected_item)['values'][0] - 1
    
    try:
        # Check if index is valid and remove the point
        if 0 <= row_id < len(DATA_POINTS):
            DATA_POINTS.pop(row_id)
            update_data_table(data_tree)
        else:
            # Should not happen if data_tree is updated correctly
            messagebox.showerror("Error", "Selected row index is invalid.")
            
    except Exception as e:
        messagebox.showerror("Error", f"Could not remove point: {e}")


def calculate_and_plot():
    """Performs the multi-point growth rate calculation and generates the plot."""
    # Reset result label
    result_label.config(text="Calculating...", fg="blue")
    
    # 1. Prepare data
    try:
        if len(DATA_POINTS) < 2:
            messagebox.showwarning("Data Error", "Please enter at least two data points for the fit.")
            result_label.config(text="Calculation Failed", fg="red")
            return

        times = [t for t, c in DATA_POINTS]
        concentrations = [c for t, c in DATA_POINTS]
        unit_time = time_unit_var.get()

        # 2. Perform calculation using SciPy fitting
        k_fit, r_squared = growth_rate_fit(times, concentrations)

        # 3. Update result display
        result_label.config(
            text=f"Fitted k: {k_fit:.4f} gen/{unit_time} (R²: {r_squared:.4f})",
            fg="purple"
        )

        # 4. Generate Plot
        fig.clear()
        ax = fig.add_subplot(111)

        # Get log-transformed concentrations for plotting the linear fit
        log2_concentrations = np.log2(concentrations)

        # Plot the data points
        ax.plot(times, log2_concentrations, 'o', label='Data Points (log2(N))')

        # Calculate the linear fit line (y = kx + b)
        # We need the intercept for the line equation, which is not returned by growth_rate_fit
        # Let's re-run linregress just for the line plotting data
        slope, intercept, _, _, _ = linregress(times, log2_concentrations)
        
        # Create a line of best fit for plotting
        x_fit = np.linspace(min(times), max(times), 100)
        y_fit = slope * x_fit + intercept

        # Plot the fitted line
        ax.plot(x_fit, y_fit, 'r-', label=f'Linear Fit (k={k_fit:.4f})')

        # Set plot labels and title
        ax.set_xlabel(f"Time ({unit_time})")
        ax.set_ylabel("Log₂ Concentration (log₂(N))")
        ax.set_title(f"Growth Curve Linear Fit (k={k_fit:.4f})")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        # Redraw the canvas
        canvas.draw()

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
        result_label.config(text="Calculation Failed", fg="red")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        result_label.config(text="Calculation Failed", fg="red")


# --- Defining the Graphical User Interface (GUI) ---

root = tk.Tk()
root.title("Microbial Growth Rate Calculator (SciPy Fit)")
# Configure grid layout manager
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

# Main frame for data entry (top)
entry_frame = ttk.LabelFrame(root, text="1. Enter Time Series Data")
entry_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)
entry_frame.grid_columnconfigure(1, weight=1)
entry_frame.grid_columnconfigure(3, weight=1)

# Data Entry Widgets
# Time (t)
ttk.Label(entry_frame, text="Time (t):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_time_t = ttk.Entry(entry_frame)
entry_time_t.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

# Concentration (N)
ttk.Label(entry_frame, text="Concentration (N):").grid(row=0, column=2, padx=5, pady=5, sticky='w')
entry_conc_N = ttk.Entry(entry_frame)
entry_conc_N.grid(row=0, column=3, padx=5, pady=5, sticky='ew')

# Add Point Button
add_button = ttk.Button(entry_frame, text="Add Point", command=add_data_point)
add_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

# Remove Point Button
remove_button = ttk.Button(entry_frame, text="Remove Selected", command=remove_data_point)
remove_button.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky='ew')

# Time Unit Selection
time_unit_var = tk.StringVar(value=ALLOWED_TIME_UNITS[0])
ttk.Label(entry_frame, text="Time Unit:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
time_unit_combo = ttk.Combobox(
    entry_frame,
    textvariable=time_unit_var,
    values=ALLOWED_TIME_UNITS,
    state="readonly"
)
time_unit_combo.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
time_unit_combo.set(ALLOWED_TIME_UNITS[0]) # Ensure default is set


# Frame for the Data Table (middle left)
table_frame = ttk.LabelFrame(root, text="2. Data Points")
table_frame.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')
table_frame.grid_columnconfigure(0, weight=1)
table_frame.grid_rowconfigure(0, weight=1)

# Data Table (Treeview)
data_tree = ttk.Treeview(table_frame, columns=("Index", "Time", "Concentration"), show='headings')
data_tree.heading("Index", text="#", anchor=tk.W)
data_tree.heading("Time", text="Time (t)", anchor=tk.W)
data_tree.heading("Concentration", text="Conc. (N)", anchor=tk.W)
data_tree.column("Index", width=40, stretch=tk.NO)
data_tree.column("Time", width=80, stretch=tk.YES)
data_tree.column("Concentration", width=100, stretch=tk.YES)
data_tree.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

# Add Scrollbar
tree_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=data_tree.yview)
data_tree.configure(yscrollcommand=tree_scrollbar.set)
tree_scrollbar.grid(row=0, column=1, sticky='ns')


# Frame for Calculation Button and Result (middle right)
calc_frame = ttk.Frame(root)
calc_frame.grid(row=1, column=1, padx=10, pady=5, sticky='nsew')
calc_frame.grid_columnconfigure(0, weight=1)

# Calculate Button
calculate_button = ttk.Button(calc_frame, text="3. Calculate & Plot Growth Rate (k)", command=calculate_and_plot)
calculate_button.grid(row=0, column=0, pady=10, padx=5, sticky='ew')

# Result Label
result_label = ttk.Label(calc_frame, text="Enter data points and click Calculate.", font=('Arial', 10, 'bold'))
result_label.grid(row=1, column=0, pady=5, padx=5, sticky='ew')


# Frame for Plot (bottom)
plot_frame = ttk.LabelFrame(root, text="4. Growth Curve Fit")
plot_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
plot_frame.grid_columnconfigure(0, weight=1)
plot_frame.grid_rowconfigure(0, weight=1)


# Matplotlib figure and canvas
fig = plt.figure(figsize=(6, 4), dpi=100)
# Create a dummy plot to initialize the canvas properly
ax_dummy = fig.add_subplot(111)
ax_dummy.text(0.5, 0.5, 'Click "Calculate & Plot" to see results.', 
              horizontalalignment='center', verticalalignment='center', 
              transform=ax_dummy.transAxes)
ax_dummy.set_title("Growth Curve Fit")
ax_dummy.set_xlabel("Time")
ax_dummy.set_ylabel("Log₂ Concentration")
ax_dummy.grid(True, linestyle='--', alpha=0.6)


canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)


# Start the GUI event loop
root.mainloop()