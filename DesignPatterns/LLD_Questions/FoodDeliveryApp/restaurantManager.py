from restaurant import Restaurant
from enums.rating import Rating
from location import Location

class RestaurantManager:
    def __init__(self):
        self._restaurants = []
        
    def create_restaurant(name:str,food_items:list,location:Location, rating:Rating)->Restaurant:
        return Restaurant(name,food_items,location,rating)
    
    def search_restaurant(name:str)->list[Restaurant]:
        return [r for r in ]
    def add_items_to_list()->None:pass
    def remove_items_from_list()->None:pass
