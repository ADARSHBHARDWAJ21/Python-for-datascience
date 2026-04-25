#abstraction - hides imlplementation part
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(' Car engine is started')
        
    def move(self):
        print('Car is moving')


c = Car()   
print(c.start_engine())   
print(c.move())
# difference between encapsulation and abstraction
# encapsulation focuses on data protection .Focuses on bundled
#data+ methods and restrict data aceess

#Abstraction - Focuses on design part I know what i can do  but not know how it is implemented
