class RideManager:
    def __init__(self) -> None:
        print('Ride manager activated')
        self.__available_cars=[]
        self.__available_bikes=[]
        self.__available_cng=[]

    def add_a_vechile(self,vechile_type,vechile):

        if vechile_type=='car':
            self.__available_cars.append(vechile)
        elif vechile_type=='bike':
              self.__available_bikes.append(vechile)
        else:
              self.__available_cng.append(vechile)
    def get_available_car(self):
        return self.__available_cars

    def find_a_vechile(self,rider,vechile_type,destination):
        if vechile_type == 'car':
            if len(self.__available_cars)==0:
                print('sorry no cars is available')
                return False
        for car in self.__available_cars:
            print('potential',rider.location,car.driver.location)
            if abs(rider.location-car.driver.location)<30:
                print('find a match for you')
                return True
                


        
uber=RideManager()