Modular Growth Rate Calculator (Python, SciPy, Matplotlib)
This project calculates the specific growth rate ($k$) of a cell or bacterial population using two methods:
Single-Point Calculation: Based on initial ($N_0$) and final ($N_t$) concentrations over a time period ($t$).
Multi-Point Fit (New): Uses linear regression (SciPy) on multiple time-series data points to find the best-fit growth rate ($k$) and displays the result with a plot (Matplotlib).
Project Structure
calculator_logic.py: The business logic. Contains the core functions: growth_rate (single point) and growth_rate_fit (multi-point SciPy linear regression).
growth_rateGUI.py: The main program (GUI). A full application using Tkinter and Matplotlib to accept multiple data points, calculate the fit, and display the growth curve plot.
test_calculator_logic.py: Contains unit tests for both calculation functions using the pytest framework.
growth_rate_ainterctive with input .py: Simple interactive CLI for the single-point calculation. (Unchanged, relies on calculator_logic.py).
growth_rate_command_line.py: Simple CLI for the single-point calculation using arguments. (Unchanged, relies on calculator_logic.py).
Installation
The new multi-point fitting functionality and plotting require external libraries.
Prerequisites
You must have Python 3 installed.
Installing Dependencies
Install the required third-party libraries using pip:
pip install scipy matplotlib pytest numpy




How to Run the Application
The primary way to use the enhanced application is through the GUI.
Run the GUI:
python growth_rateGUI.py





Usage: Enter your time and concentration data points one by one, clicking "Add Point" for each pair. Select the appropriate time unit. When ready, click "Calculate & Plot Growth Rate (k)" to see the fitted growth rate and the corresponding graph.
How to Run Tests
To ensure the calculation logic is correct, run the unit tests using pytest:
pytest test_calculator_logic.py





You should see output indicating that all tests have passed.
AI Usage and Prompts
The following prompts were used to evolve the project from the uploaded state to the current state, following the provided instructions:


Step
Prompt Provided to AI (Gemini 2.5)
Purpose
1.
Enhance the calculator_logic.py file. Add a new function called growth_rate_fit that calculates the specific growth rate ($k$) using a set of multiple time and concentration points. This function MUST use scipy.stats.linregress to perform a linear fit on the $\log_2$-transformed concentration data over time. The function should take two lists (time points, concentration points) and return a tuple of (k, R-squared). Add input validation for lists (length, non-positive values).
Integrating SciPy for multi-point calculation.
2.
Create a new file test_calculator_logic.py using pytest. Write comprehensive unit tests for both the existing growth_rate(Nt, N0, t) function and the new growth_rate_fit(times, concentrations) function. Ensure tests cover edge cases like zero/negative inputs and mismatched list lengths.
Adding Unit Tests and ensuring testability.
3.
Update growth_rateGUI.py. Modify the Tkinter interface to allow users to input multiple (time, concentration) data points and store them in a list. Replace the old single-point calculation with a button that calls the new growth_rate_fit function and uses matplotlib to display a plot of the $\log_2(N)$ vs $t$ data with the fitted linear regression line. The plot should be embedded in the GUI using FigureCanvasTkAgg.
Updating GUI for multi-point input and Adding Plotting (Matplotlib).
4.
Update the README.md to explain the new file structure, the use of SciPy and Matplotlib, the installation steps (pip install scipy matplotlib pytest numpy), and the instructions for running the GUI and the tests. Also, include this table detailing the AI prompts used.
Finalizing Documentation.

Post-Development Debugging (Critical Fix)
Step
Issue
Fix Applied to calculator_logic.py
5.
Test Failure: The test test_growth_rate_fit_stagnant_data_k0 failed due to NaN (Not a Number) being generated for the $R$-squared value when all concentration data points were identical (zero variance/stagnant growth).
Solution: Added an explicit check within growth_rate_fit to determine if all $\log_2$ concentration values are the same. If they are, the function returns a hardcoded $k=0.0$ and $R^2=1.0$. This prevents the SciPy division-by-zero error and correctly reflects the perfect fit of a horizontal line to static data.


