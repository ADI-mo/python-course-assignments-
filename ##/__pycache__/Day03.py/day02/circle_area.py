from math import pi
def circle_area(radius, pi_val=3.14): # Function and parameters are now lower case
    """
    Calculate the area of a Circle using Radius .
    
    Formula: Area = pi *Radius**2 
    
    Args:
        radius (float): The Radius of the Circle # Parameter name updated in docstring
        pi_val (float):the volue of pi (default is 3.14 ) # Parameter name updated in docstring
    Returns:
        float: The area of the Circle
    """
    # Calculation uses the parameter value (pi_val) as in the original logic, 
    # but the variable names are now lowercase.
    area =(pi_val *(radius**2)) 
    return area


# Example usage
if __name__ == "__main__":
    #pass
    #...
    # Get base and height from user input
    try:
        radius = float(input("Enter the Radius of the Circle: ")) # Variable is now lower case
        # Calculate and display the area
    # ... (הקוד עד שורת ה-print) ...
        area = circle_area(radius) # Variable is now lower case
        print(f"Circle with Radius {radius} has area: {area}")
        
    # שורה קריטית זו חייבת להגיע מיד אחרי ה-try-block
    except ValueError: 
        print("Please enter a valid number for the Radius.")#בבבב8
