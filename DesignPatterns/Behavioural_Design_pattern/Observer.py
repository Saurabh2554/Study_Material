"""
The Observer Design Pattern is one of the most commonly used behavioral design patterns in software development. It is particularly useful when you want to establish a one-to-many relationship between objects. This allows an object (known as the subject) to notify other objects (known as observers) when there is a change in its state. The Observer pattern is widely used in event-driven programming, GUIs, and even in messaging systems like Kafka.

https://devcookies.medium.com/observer-design-pattern-a-complete-guide-with-examples-ec40648749ff

https://chatgpt.com/c/68ea7dce-6168-8322-8e15-b7f773937493

"""
from abc import ABC, abstractmethod

class IObserver(ABC):
    @abstractmethod
    def update(self, temp, press)->None:pass

    @abstractmethod
    def display(self)->None:pass

class IObservable(ABC):
    @abstractmethod
    def add_observer(self,observer:IObserver)->None:pass

    @abstractmethod
    def remove_observer(self,observer:IObserver)->None:pass

    @abstractmethod
    def notify(self)->None:pass

    @abstractmethod
    def set_metrics(self, temp:int, press:int):pass
    
class WeatherStation(IObservable):
    def __init__(self):
        self.__observer = []
        self.__temp = 50
        self.__pressure = 30

    def add_observer(self,observer:IObserver):
        self.__observer.append(observer)

    def remove_observer(self, observer: IObservable):
        self.__observer.remove(observer)  

    def notify(self):
        for obs in self.__observer:
            obs.update(self.__temp, self.__pressure)
    
    def set_metrics(self, temp, press):
        self.__temp = temp
        self.__pressure = press
        self.notify()
            

class WeatherDisplay(IObserver):
    def __init__(self):
        self.__temp = 0
        self.__pressure = 0

    def update(self, temp, press)->None:
        self.__temp = temp
        self.__pressure = press
        self.display()

    def display(self)->None:
        print(f"Current temperature is: {self.__temp} and pressure is: {self.__pressure}.")    



def observer_pattern_demo():
    display1:WeatherDisplay = WeatherDisplay()
    diaplay2:IObserver = WeatherDisplay()

    weatherStation:IObservable = WeatherStation()

    weatherStation.add_observer(display1)
    weatherStation.add_observer(diaplay2)
    display1.display()
    diaplay2.display()

    weatherStation.set_metrics(35, 40)


if __name__ == "__main__":
    print("main")
    observer_pattern_demo()
