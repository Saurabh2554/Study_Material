from dataclasses import dataclass

@dataclass
class Location:
    address: str
    pincode: str
    latitude: float
    longitude: float

    
