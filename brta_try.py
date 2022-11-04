
import random
class BRTA:
    def __init__(self) -> None:
      self.__store_dict={}
    
    def take_driving_test(self,name,email):
        self.name=name
        score=random.randint(0,500)
        if score>=33:
            print('Congrats You paseed Your score',score) 
            license_number=random.randint(500,1120)
            self.__store_dict[email]=license_number
            return license_number

        else:
            print('Your faild your score ',score)
            return False

    def valid_user_check(self,email,license):
        for key,value in self.__store_dict.items():
          if key==email and value ==license:
            return True

        return False
