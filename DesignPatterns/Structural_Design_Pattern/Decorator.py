"""
Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
You want to add behavior or state to individual objects at run-time. Inheritance is not feasible because it is static, applies to an entire class and may lead to class explossion.

https://chatgpt.com/c/68ccd626-fccc-8329-beea-22294e9ab6c6 (Start looking from pizza example)
"""

# In decorator pattern we make both HAS-A and IS-A relation with the same base class.

"""
Problem statement: Suppose you own a pizza shop where you have multiple base pizza say margerita, veg-delight, corn etc. and for each of these you have multiple/combinations of toppings say (Margerita + Extra cheese), (Margerita + Mushroom), (Margerita + Mushroom +Extra cheese) etc, and you need to calculate the cost of each combination. 
How will you implement this?
"""

"""
Answer: In order to implement the above scenario so that it can scale headlessly, we can use decorator pattern where we will have a base pizza(Abstract class/ Interface) and one base Toppings(Abstract class/ Interface). The toppings will be making HAS-A and IS-A relation with base pizza, because base_pizza + Extracheese in itself a base_pizza for other say (Margerita + Mushroom +Extra cheese), and HAS-A relation is explained as toppings can not exist independently as topping must have a base pizza.
"""

from abc import ABC, abstractmethod

# Base_Pizza interface
class IBasePizza(ABC):
    @abstractmethod
    def cost(self)->int:pass

# multiple Base_Pizza implementation
class Margerita(IBasePizza):
    def cost(self)->int:
        return 120

class VegDelight(IBasePizza):
    def cost(self)->int:
        return 140

class CornBase(IBasePizza):
    def cost(self)->int:
        return 80


#Toppings interface


class ITopings(IBasePizza):pass
    #Case -01: define a personal cost method for each toppings and hence it does not require IS-A relation
    # @abstractmethod
    # def cost()->int:pass


class Extracheese(ITopings):
    def __init__(self, base_pizza: IBasePizza):
        self.base_pizza = base_pizza
    
    # Base_Pizza cost method
    def cost(self)->int:
        return self.base_pizza.cost() + 40    

class Mushroom(ITopings):
    def __init__(self, base_pizza: IBasePizza):
        self.base_pizza = base_pizza
    
    # Base_Pizza cost method
    def cost(self)->int:
        return self.base_pizza.cost() + 30    


def main():
    # Case-01: Calculate cost of veg Delight
        
        pizza = VegDelight()
        print(pizza.cost())

    # Case -02: Calculate cost of Margerita + Extracheese
        """
        Here in order to calculate cost we can do two things as,  firstly make a cost method in Toppings and let them define their own cost. But we can lead to serious problem here and that is we will end up creating multiple objects which may led to slowdown our app. Visualise in case where you are adding multiple toppings say 4 or 5 toppings.

        Ex: 
          pizza = Margerita()
          topping = Extracheese()

          final_cost = pizza.cost() + topping.cost() 

        The other approach could be let the Toppings extend the IBasePizza and override that cost method for your own implementtion.

        """
        pizza = Extracheese(Margerita())
        print(pizza.cost())


if __name__ == "__main__":
    main()


