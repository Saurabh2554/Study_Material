from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def drive(self)->None:pass


class Car(IVehicle):
    def drive(self)->None:
        print("driving car")


class Bike(IVehicle):
    def drive(self)->None:
        print("Riding bike")


class Bus(IVehicle):
    def drive(self)->None:
        print("Driving bus")

class IVehicleFactory(ABC):
    @abstractmethod
    def create(self) -> IVehicle:pass

class BikeFactory(IVehicleFactory):
    def create(self)->IVehicle:
        return Bike()

class BusFactory(IVehicleFactory):
    def create(self)->IVehicle:
        return Bus()    


def VehicleFactoryTest(vehicle:str):
    bikeFactory = BikeFactory()
    bike = bikeFactory.create()
    bike.drive()



if __name__ == "__main__":
    VehicleFactoryTest("buS")
    
  