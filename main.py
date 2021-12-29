# conding: utf-8

from car import Car

parking = list()

for  i in range(0, 5):
    OBJ = Car()
    parking.append(OBJ)

parking[0].set_model('Monza')
parking[0].set_color('blue')
parking[0].set_year(1992)
parking[0].set_year('1993')
parking[0].set_year('aaaa')

Car.total()
del parking[1]

for Carr in parking:
    print(Carr.get_model() + ' - ' + Carr.get_year())

Car.stotal(parking[0])