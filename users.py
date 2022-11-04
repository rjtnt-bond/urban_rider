import hashlib
from brta import BRTA
from random import randint
from Vechiles import car,Bike,cng
from ride_manager import uber

license_authorety=BRTA()
class Users:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        self.password=password
        pass_sotre=hashlib.md5(password.encode()).hexdigest()
        with open('store.txt','a') as writfile:
              writfile.write(f'{email} {pass_sotre}\n')
        writfile.close()
        print(f'{name} User profile create successfully')
        
    @staticmethod
    def log_in(email,password):
        store_password=''
        with open('store.txt','r') as readfile:
            lines=readfile.readlines()
            for line in lines:
                if email in line:
                    store_password=line.split(' ')[1]
        readfile.close()
        hashed_pass=hashlib.md5(password.encode()).hexdigest()

        if hashed_pass==store_password:
            print('Valid Users')
            return True
        else:
            print('Invalid Users')
            return False


class Riders(Users):

    def __init__(self, name, email, password,balance,location) -> None:
        self.balance=balance
        self.location=location
        super().__init__(name, email, password)

    def get_location(self):
        return self.location

    def set_loction(self,location):
        self.location=location

    def request_trip(self,destination):
        pass

    def start_trip(self,fare):
        self.balance-=fare


class Drivers(Users):
    def __init__(self, name, email, password,location,license) -> None:
        self.location=location
        self.license=license
        self.valid_driver=license_authorety.valid_license(email,license)
        self.earing=0
        super().__init__(name, email, password)

    def start_a_trip(self,destination,fare):
        self.earing+=fare
        self.loaction=destination


    def taking_drinving_test(self):
        result=license_authorety.take_driving_test(self.email)
        if result==False:
            print('Sorry You Have to Failed try again')
        else:
            print('Its your license ')
            self.license=result
            self.valid_driver=True

    def register_a_vechile(self,vechile_type,license_plat,rate):
        if self.valid_driver is True:
            if vechile_type=='car':
                new_vehicle=car(license_plat,vechile_type,rate,self)
                uber.add_a_vechile(vechile_type,new_vehicle)
            elif vechile_type=='bike':
                new_vehicle=Bike(license_plat,vechile_type,rate,self)
                uber.add_a_vechile(vechile_type,new_vehicle)
            else:
                new_vehicle=cng(license_plat,vechile_type,rate,self)
                uber.add_a_vechile(vechile_type,new_vehicle)


        else:
            print('Your are not valid driver ')
            
    


rider1=Riders('rider1','rider@1','asdjh',40,randint(0,300))
rider2=Riders('rider2','rider@2','astjh',40,randint(0,300))


driver1=Drivers('driver1','driver1@gmail.com','abcde',randint(0,100),5345)
driver1.taking_drinving_test()
driver1.register_a_vechile('car',234,34)


driver2=Drivers('driver2','driver2@gmail.com','abcde',randint(0,100),5345)
driver2.taking_drinving_test()
driver2.register_a_vechile('car',234,34)

driver3=Drivers('driver3','driver3@gmail.com','abcde',randint(0,100),5345)
driver3.taking_drinving_test()
driver3.register_a_vechile('car',264,34)

print(uber.get_available_car())
uber.find_a_vechile(rider1,'car',90)



