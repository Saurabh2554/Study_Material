"""
Full research:
https://chatgpt.com/g/g-p-6839f818d834819192daad29c23130b3-saurabh-research/c/68850968-fcdc-832c-be1e-9b773208e395
"""

import threading

class SingletonWithThreadLock:
    _instance = None
    _lock = threading.Lock()  # Lock for thread safety


    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        else:
            print("instance already exist! returning the same")    
        return cls._instance

    def __init__(self, first_name, last_name):
        print(f"Started: __init__ method of Human class with self: {self}")
        self.first_name = first_name
        self.last_name = last_name
        print(f"Ended: __init__ method of Human class")



# Eager Initialization
class Singleton:
    # Eagerly create the instance when the class is defined
    _instance = None

    def __init__(self, first_name, last_name):
        print(f"Started: __init__ with self: {self}")
        self.first_name = first_name
        self.last_name = last_name
        print(f"Ended: __init__")

    @classmethod
    def get_instance(cls):
        return cls._instance


# Eagerly create the instance with default values
Singleton._instance = Singleton("John", "Doe")  # <-- eager creation

# Usage
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print(s1 is s2)  # True
print(s1._instance, " " ,s2._instance)
