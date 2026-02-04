from dataclasses import dataclass
from location import Location
from enums.rating import Rating
@dataclass
class Restaurant:
    name: str
    foodItems:list
    location: Location
    rating: Rating

