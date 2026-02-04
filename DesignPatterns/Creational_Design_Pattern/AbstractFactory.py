"""
When to Use Abstract Factory
🔸When your application needs to create families of related or dependent objects.

🔸When you want to ensure consistency among related objects.

🔸When the object creation logic needs to be decoupled from the client code.

🔸When your system needs to be scalable, with the possibility of introducing new families of objects.

Use-Cases
1. Cross-Platform GUIs:
🔸A GUI toolkit might need to create buttons and text fields for different operating systems (Windows, MacOS, Linux).

🔸The Abstract Factory ensures that all UI components look consistent for each OS.

2. Themed Applications:
🔸Applications with light and dark themes often use Abstract Factory to create components (e.g., buttons, menus) matching the selected theme.

3. Database Abstraction:
🔸A factory can create different database connectors (e.g., MySQL, PostgreSQL) depending on configuration.

https://medium.com/@kalanamalshan98/abstract-factory-design-pattern-the-ultimate-guide-for-beginners-4b0f97694b00
"""

"""
Imagine a furniture store that offers two collections:

Modern Furniture: Sleek designs with minimalist features.
Victorian Furniture: Elegant, traditional designs.
The Problem
When a customer chooses a collection (Modern or Victorian), they expect matching chairs and tables. Hardcoding the manufacturing of each type of furniture for every collection would be inefficient.

Here we are creating families(Modern , Victorian Furniture) or related objects(Chair, Table) that is families of chair and table for different designs.

"""


from abc import ABC, abstractmethod

class IChair(ABC):
    @abstractmethod
    def sitOn(self)->None:pass

class ITable(ABC):
    @abstractmethod
    def sitOn(self)->None:pass

class ModernChair(IChair):
    def sitOn(self)->None:
        print("sitting on modern chair.")

class ModernTable(ITable):
    def sitOn(self)->None:
        print("Using modern table")

class VictorianChair(IChair):
    def sitOn(self)->None:
        print("sitting on Victorian chair.")   

class VictorianTable(ITable):
    def sitOn(self)->None:
        print("Using Victorian table")     

class IFurnitureFactory(ABC):
    @abstractmethod
    def createChair(self)->IChair:pass

    @abstractmethod
    def createTable(self)->ITable:pass

class ModernFurnitureFactory(IFurnitureFactory):
    def createChair(self)->IChair:
        return ModernChair()
    
    def createTable(self)->ITable:
        return ModernTable()


class VictorianFurnitureFactory(IFurnitureFactory):
    def createChair(self)->IChair:
        return VictorianChair()
    
    def createTable(self)->ITable:
        return VictorianTable()
    
def main():
    # create modern chair and victorian table
    print("creating modern chair and victorian table")
    modernFurniture:IFurnitureFactory = ModernFurnitureFactory()
    modernChair:IChair = modernFurniture.createChair()
    modernChair.sitOn()  

    victorianFurniture:IFurnitureFactory = VictorianFurnitureFactory()
    victorianTable:ITable = victorianFurniture.createTable()
    victorianTable.sitOn() 

    #Create Victorian table and victorian chair
    print("creating Victorian table and victorian chair")
    victorianFurniture:IFurnitureFactory = VictorianFurnitureFactory()
    victorianTable:ITable = victorianFurniture.createTable()
    victorianTable.sitOn()

    victorianFurniture:IFurnitureFactory = VictorianFurnitureFactory()
    victorianChair:IChair = victorianFurniture.createChair()
    victorianChair.sitOn()

if __name__ == "__main__":
    main()