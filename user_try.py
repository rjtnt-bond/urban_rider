
import hashlib
from brta_try import BRTA
license_authorety=BRTA()

class User:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        self.passwrod=password
       
        self.stor_pass=hashlib.md5(password.encode()).hexdigest()

        with open('store.txt','w') as writefile:
            writefile.write(f'{email} {self.stor_pass}')
        writefile.close()

    @staticmethod
    def log_in(email,password):
        store_pass=''
        with open('store.txt','r') as readfile:
            lines=readfile.readlines()
            for line in lines:
                if email==line.split(' ')[0]:
                    store_pass=line.split(' ')[1]

        readfile.close()
        hashed_password=hashlib.md5(password.encode()).hexdigest()
        if store_pass==hashed_password:
            print('Valid User ')
            return True
        else:
            print('Invaild User ')
            return False
            
class Riders(User):
    def __init__(self, name, email, password,balance,location) -> None:
        self.location=location
        self.balance=balance
        super().__init__(name, email, password)


    def get_loaction(self):
       pass

    def set_location(self,location):
        self.location=location
    def request_trip(self,destination):
        pass

    def star_trip(self,fare):
        self.balance-=fare


class drivers(User):
    def __init__(self, name, email, password,location,licence) -> None:
        self.location=location
        self.license=licence
        self.valid_user=license_authorety.valid_user_check(email,licence)
        self.earing=0
        super().__init__(name, email, password)

    def start_a_trip(self,destination,fare):
        self.balance+=fare
        self.location=destination

    def testing_driver(self):
        result=license_authorety.take_driving_test(self.email)
        if result== False:
            print('Sorry Your Vaild')
        else:
            print('Your Licnese')
            self.license=result
            self.valid_user=True


lallusing=User('Lalu','lalu67@gamil.com','asjdhs7354')
lallusing.log_in('lalu67@gamil.com','asjdhs7354')

akkas=drivers('Bondhon','kanu@34.cgiml.com','dsjkfhsj56','dhaka','iuefysdh346r')
res=license_authorety.valid_user_check('kanu@34.cgiml.com','iuefysdh346r')
print(res)
res1=license_authorety.take_driving_test('Bondhon','kanu@34.cgiml.com')
 
res=license_authorety.valid_user_check('kanu@34.cgiml.com',res1)
print(res)


    