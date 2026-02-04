from enum import Enum

class Rating(Enum):
    ONE = (1, "Poor")
    TWO = (2, "Average")
    THREE = (3, "Good")
    FOUR = (4, "Very Good")
    FIVE = (5, "Excellent")

    def __init__(self, value, label):
        self._value_ = value
        self.label = label

    def __str__(self):
        return f"{self.value} - {self.label}"