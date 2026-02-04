class Human:
    def __new__(cls, *args, **kwargs):
        print(f"Creating the object with cls: {cls} and args: {args}")
        obj = super().__new__(cls)
        print(f"Object created with obj: {obj} and type: {type(obj)}")
        return obj

    def __init__(self, first_name, last_name):
        print(f"Started: __init__ method of Human class with self: {self}")
        self.first_name = first_name
        self.last_name = last_name
        print(f"Ended: __init__ method of Human class")

human_obj = Human("Virat", "Kohli")

# type's call method simulation

# type's __call__ method which gets called when Human class is called i.e. Human()
def __call__(cls, *args, **kwargs):
    # cls = Human class
    # args = ["Virat", "Kohli"]
    # Calling __new__ method of the Human class, as __new__ method is not defined
    # on Human, __new__ method of the object class is called
    human_obj = cls.__new__(*args, **kwargs)

    # After __new__ method returns the object, __init__ method will only be called if
    # 1. human_obj is not None
    # 2. human_obj is an instance of class Human
    # 3. __init__ method is defined on the Human class
    if human_obj is not None and isinstance(human_obj, cls) and hasattr(human_obj, '__init__'):
        # As __init__ is called on human_obj, self will be equal to human_obj in __init__ method
        human_obj.init(*args, **kwargs)

    return human_obj


"""  
So, following steps are followed while creating and initializing an object in Python:

Since Human class is callable, bcoz it's parent(objec)


1. Call the Human class - Human(); this internally calls the __call__ method of the type class (i.e., type.__call__(Human, "Virat", "Kohli")).
2. type.__call__ will first call the __new__ method defined on the Human class. If the __new__ method is not defined on the Human class, the __new__ method of the object class will be called.
3. The __new__ method will the return the object of type Human i.e. human_obj
4. Now, type.__call__ will call the __init__ method defined on the Human class with human_obj as the first argument. This human_obj will be self in the __init__ method.
5. The __init__ method will initialize the human_obj with the first_name as Virat and thelast_name as Kohli. The __init__ method will not return anything.
6. In the end, type.__call__ will return the human_obj object.  

Docs Ref: https://www.honeybadger.io/blog/python-instantiation-metaclass/

"""

"""
Here Human class is itself an instance of type class(Meta class). 
So when we print type(Human) it prints: <class 'type'>

Also Human class implicitely inherits from python global Object's class.
So when we print Human.__bases__ it prints: (<class 'object'>,)

Human class is an instance of type class and tyep class is an instance of itself and type class also inherits from objects class.
print(type.__bases__) # Output: (<class 'object'>,)

Object class does not inherits from any class and is the parent most class in Cpython
Also Python object class is an instance of type class:
print(object.__class__) # Output: <class 'type'>

Finally:
object is an instance of type
type is a subclass of object


"""