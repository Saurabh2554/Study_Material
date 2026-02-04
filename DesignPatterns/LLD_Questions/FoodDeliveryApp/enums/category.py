from enum import Enum

class FoodCategory(Enum):
    VEG = "Vegetarian"
    NON_VEG = "Non-Vegetarian"
    FASTING = "Fasting Special"
    VEGAN = "Vegan"    
    JAIN = "Jain"

    def __str__(self):
        return self.value
    