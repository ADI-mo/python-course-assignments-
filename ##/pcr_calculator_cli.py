import argparse
from pcr_calculator import PCRCalculator

def display_results(num_reactions):
    # Get volumes from calculator
    volumes = PCRCalculator.calculate_volumes(num_reactions)
    
    # Display results
    print("\nResults (safety factor of 10% included):")
    print("-" * 40)
    for component in PCRCalculator.COMPONENTS:
        print(f"{component}:\t{volumes[component]:.2f} µL")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='PCR Reaction Calculator')
    parser.add_argument('--value', type=float, help='Number of reactions')
    
    args = parser.parse_args()
    
    # If no argument provided, ask for input
    if args.value is None:
        while True:
            try:
                num_reactions = float(input("Enter number of reactions: "))
                if num_reactions > 0:
                    break
                print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        num_reactions = args.value
    
    display_results(num_reactions)

if __name__ == "__main__":
    main()