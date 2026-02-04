"""AN Example of Simle Builder."""
"""In real world this concept is used while creating queryset in django. EX: .filter().order_by()"""
"""
The Builder Design Pattern is a creational pattern that provides a step-by-step approach to constructing complex objects. 
It separates the construction process from the object’s representation, enabling the same process to create different variations of an object. 
This pattern is especially useful when an object requires multiple steps or configurations during creation.

Encapsulates object construction logic in a Builder class.
Allows flexible and controlled object creation.
Supports creation of different representations of a product using the same construction process.
Improves readability and maintainability by avoiding large constructors with many parameters.


Use cases
🔸SQL query builders, like those found in ORMs (Object-Relational Mappers) such as Laravel's Eloquent or SQLAlchemy in Python, utilize the Builder pattern to construct SQL queries dynamically. 
This allows developers to chain methods like select(), where(), limit(), and orderBy() to build complex queries in a readable manner.

🔸When creating user interface components like dialog boxes, forms, or custom widgets, the Builder pattern can be used to assemble elements (buttons, text fields, images) and apply styles in a structured way.

"""

from __future__ import annotations
from abc import ABC, abstractmethod

class PC:
    def __init__(self, cpu, gpu, ram, storage):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage

    def show_config(self):
        print(f"CPU: {self.cpu}, GPU: {self.gpu}, RAM: {self.ram}, Storage: {self.storage}")


class IPCBuilder(ABC):
    @abstractmethod
    def set_cpu(self, cpu:str)->IPCBuilder:pass
    @abstractmethod
    def set_gpu(self, gpu:str)->IPCBuilder:pass
    @abstractmethod
    def set_storage(self, storage:str)->IPCBuilder:pass
    @abstractmethod
    def set_ram(self, ram:str)->IPCBuilder:pass


class CustomPCBuilder(IPCBuilder):
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.storage = None
        self.ram = None

    def set_cpu(self, cpu:str)-> IPCBuilder:
        self.cpu = cpu
        return self

    def set_gpu(self, gpu:str)-> IPCBuilder:
        self.gpu = gpu
        return self

    def set_ram(self, ram:str)-> IPCBuilder:
        self.ram = ram
        return self

    def set_storage(self, storage:str)-> IPCBuilder:
        self.storage = storage
        return self

    def build(self)->PC:
        return PC(self.cpu, self.gpu, self.storage, self.ram)   


def client()->None:
    builder = CustomPCBuilder()
    pc = (builder.set_cpu("Ryzen 7")
                .set_gpu("RTX 4060")
                .set_ram("16GB")
                .set_storage("1TB NVMe")
                .build())

    pc.show_config()

if __name__ == "__main__":
    client()


  