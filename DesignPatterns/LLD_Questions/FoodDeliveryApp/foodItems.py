from dataclasses import dataclass
from enums import FoodCategory, Rating, Cuisine

@dataclass
class FoodItem:
    name:str
    category:FoodCategory
    price:float
    rating:Rating
    cuisine:Cuisine
    
