#Write a program which calculates toll calculation on some location following is data provided:

from abc import ABC , abstractmethod

class Vehicle(ABC):
    def __init__(self,persons):
        self.persons=persons

    @abstractmethod
    def calculate_toll(self):
        pass

class TwoWheeler(Vehicle):
    def calculate_toll(self):
        toll = 20

        if self.persons >= 2:
            toll += (self.persons -2)*10
        return toll

class ThreeWheeler(Vehicle):
    def calculate_toll(self):
        toll = 30
        if self.persons >= 3:
            toll += (self.persons -3)*20
        return toll


class FourWheeler(Vehicle):
    def calculate_toll(self):
        toll = 40
        if self.persons >= 4:
            toll += (self.persons -4)*40
        return toll

class HeavyVehicle(Vehicle):
    def calculate_toll(self):
        toll = 60
        if self.persons >= 6:
            toll += (self.persons -6)*100

        return toll

v1 = TwoWheeler(3)
v2 = ThreeWheeler(4)
v3 = FourWheeler(5)
v4 = HeavyVehicle(7)

print('Two Wheeler Tol:',v1.calculate_toll())
print('Three Wheeler Tol:',v2.calculate_toll())
print('Four Wheeler Tol:',v3.calculate_toll())
print('Heavy Vehicle Tol:',v4.calculate_toll())