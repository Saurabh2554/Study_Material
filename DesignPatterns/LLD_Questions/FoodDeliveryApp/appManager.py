from app import App
from threading import Lock
from restaurant import Restaurant
from location import Location

class AppManager:
    _instance = None

    def __new__(cls, app:App):
        if cls._instance is None:
            cls._instance = super(AppManager, cls).__new__(cls)
            cls._instance.app = app
        return cls._instance
    
    def add_restaurant(self, restaurant:Restaurant):
        if any(r.name.lower() == restaurant.name.lower()
            for r in self.food_delivery.restaurants):
            print(f"Restaurant '{restaurant.name}' already exists. Skipping add.")
            return False

        self.app.restaurants.append(restaurant)

    def remove_restaurant(self, restaurant_name:str):
        self.app.restaurants = [
            r for r in self.food_delivery.restaurants
            if r.name.lower() != restaurant_name.lower()
        ]

    def load_restaurants(self,location:Location)->Restaurant:
        return [r for r in self.app.restaurants if r.location.address.lower() == location.address.lower()]  
    
       


