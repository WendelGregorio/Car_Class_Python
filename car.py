# coding: utf-8
"""Class Car"""


class Car(object):
    """Car register"""
    totalCars = 0

    def __init__(self, model=None, year=None, price=None, color=None):
        """Constructor"""
        if model is None:
            self.model = "Fusca"
            self.vel_max = 80
            self.year = 1981
            self.price = 5000
            self.color = "Blue"
        else:
            self.model = model
            self.vel_max = 180
            self.year = year
            self.price = price
            self.color = color
        self.__class__.totalCars += 1

    def __del__(self):
        """Destructor"""
        self.__class__.totalCars -= 1
        print("Removing {}: endereco {}".format(self.model,id(self))) 

    def get_model(self):
        """Return the vehicle model"""
        return str(self.model)

    def set_model(self, model):
        """Assign a new model to vehicle"""
        if type(model) is str:
            self.model = model

    def get_color(self):
        """Return the vehicle color"""
        return str(self.color)

    def set_color(self, new_color):
        """Assign a new color to vehicle"""
        if type(new_color) is str:
            self.color = new_color

    def get_year(self):
        """Return the vehicle year"""
        return str(self.year)

    def set_year(self, new_year):
        """Assign a new year to vehicle"""
        if type(new_year) is int:
            self.year = new_year
        elif type(new_year) is str:
            try:
                self.year = new_year
            except ValueError:
                pass

    def __repr__(self):
        return '<{}: {} - {}>\n'.format(self.model,self.year,self.color)

    @classmethod
    def total(cls):
        """Class Method"""
        print('Total cars: ' + str(cls.totalCars))

    @staticmethod
    def stotal(class_car):
        """Static method"""
        print('Total cars:  ' + str(class_car.__class__.totalCars))

        