# Data Encapsulation

class Government:

    def __init__(self, price):  # declared like this or else def __init__(self): like that we use
        self.__price = price

    def ViewPetrolPrice(self):
        print(self.__price)

    def HikePrice(self, price):
        self.__price = price

central_govt = Government(90)
central_govt.ViewPetrolPrice()

central_govt.__price = 100     # Outside we can't change the values. Bcoz of It is in PRIVATE using of ( __price )
central_govt.ViewPetrolPrice()

central_govt.HikePrice(140)
central_govt.ViewPetrolPrice()