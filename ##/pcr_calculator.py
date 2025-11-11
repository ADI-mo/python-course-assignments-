class PCRCalculator:
    # Base volumes per reaction
    BASE_VOLUMES = {
        "2× Green Master Mix": 7.5,
        "Primer Forward (10 µM)": 0.5,
        "Primer Reverse (10 µM)": 0.5,
        "Template DNA": 1.0,
        "Water (ddH₂O)": 5.5
    }
    
    COMPONENTS = [
        "2× Green Master Mix",
        "Primer Forward (10 µM)",
        "Primer Reverse (10 µM)",
        "Template DNA",
        "Water (ddH₂O)"
    ]
    
    SAFETY_FACTOR = 1.1  # 10% extra volume for pipetting errors
    
    @staticmethod
    def calculate_volumes(num_reactions):
        """
        Calculate PCR reaction volumes for given number of reactions.
        
        Args:
            num_reactions (float): Number of reactions to calculate for
            
        Returns:
            dict: Component names as keys and calculated volumes as values
        """
        volumes = {}
        for component in PCRCalculator.COMPONENTS:
            base_volume = PCRCalculator.BASE_VOLUMES[component]
            total_volume = base_volume * float(num_reactions) * PCRCalculator.SAFETY_FACTOR
            volumes[component] = total_volume
        return volumes