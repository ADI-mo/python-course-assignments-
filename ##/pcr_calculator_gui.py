import tkinter as tk
from tkinter import ttk
from pcr_calculator import PCRCalculator

class PCRCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PCR Reaction Calculator")
        
        # Set up the main frame with padding
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create input field for number of reactions
        ttk.Label(self.main_frame, text="Number of reactions:").grid(row=0, column=0, sticky=tk.W)
        self.num_reactions = tk.StringVar(value="1")
        ttk.Entry(self.main_frame, textvariable=self.num_reactions).grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        # Create calculate button
        ttk.Button(self.main_frame, text="Calculate", command=self.calculate).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Create results display area
        res_text = "Results (safety factor of 10% included):"
        self.results_frame = ttk.LabelFrame(self.main_frame, text=res_text, padding="10")
        self.results_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Labels for results
        self.components = PCRCalculator.COMPONENTS
        
        self.result_labels = {}
        for i, component in enumerate(self.components):
            ttk.Label(self.results_frame, text=f"{component}:").grid(row=i, column=0, sticky=tk.W)
            self.result_labels[component] = ttk.Label(self.results_frame, text="0.0 µL")
            self.result_labels[component].grid(row=i, column=1, sticky=tk.E)

    def calculate(self):
        try:
            num_reactions = float(self.num_reactions.get())
            # Get volumes from calculator
            volumes = PCRCalculator.calculate_volumes(num_reactions)
            
            # Update display
            for component in self.components:
                self.result_labels[component].config(text=f"{volumes[component]:.2f} µL")
        except:
            pass

def main():
    root = tk.Tk()
    app = PCRCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()