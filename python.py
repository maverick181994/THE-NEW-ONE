class Car(object):

    __YEAR = 2017  # defining constant

    def __init__(self, make, model):
        self.make = make
        self.model = model


    def display_info(self):
     return f"car:{self.make} {self.model} {self.__YEAR}"

car_details_one = Car("Honda", "jazz")

car_details_one.year = 2019 # even if we pass a new value then only it will take the value of constant defined within a class

print(car_details_one.display_info())

