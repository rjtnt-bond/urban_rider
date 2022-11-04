from abc import ABC,abstractclassmethod

class Vehicle(ABC):
    speed={
        'car':30,
        'bike':50,
        'cng':15
    }

    def __init__(self,license_plat,Vechile_type,rate,driver) -> None:
        self.vechile_type=Vechile_type
        self.rate=rate
        self.driver=driver
        self.status='available'
        self.license_plat=license_plat
        self.speed=self.speed[Vechile_type]

    @abstractclassmethod
    def start_driving(self):
        pass

    @abstractclassmethod
    def trip_finished(self):
        pass

class car(Vehicle):
    def __init__(self, license_plat, Vechile_type, rate, driver) -> None:
        super().__init__(license_plat, Vechile_type, rate, driver)

    def start_driving(self):
        self.status='unavailable'
        print(self.vechile_type,self.license_plate,' stated')

    def trip_finished(self):
        self.status='available'
        print(self.vechile_type,self.license_plat,'completed trip')

class Bike(Vehicle):
    def __init__(self, license_plat, Vechile_type, rate, driver) -> None:
        super().__init__(license_plat, Vechile_type, rate, driver)

    def start_driving(self):
        self.status='unavailable'
        print(self.vechile_type,self.license_plate,' stated')

    def trip_finished(self):
        self.status='available'
        print(self.vechile_type,self.license_plat,'completed trip')

class cng(Vehicle):
    def __init__(self, license_plat, Vechile_type, rate, driver) -> None:
        super().__init__(license_plat, Vechile_type, rate, driver)

    def start_driving(self):
        self.status='unavailable'
        print(self.vechile_type,self.license_plate,' stated')

    def trip_finished(self):
        self.status='available'
        print(self.vechile_type,self.license_plat,'completed trip')