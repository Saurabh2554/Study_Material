from dataclasses import dataclass
from restaurant import Restaurant

@dataclass
class App:
    name:str
    restaurants:list[Restaurant]

