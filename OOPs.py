class Car:

    def __init__(self, Model, Color, Year):

        self.Model = Model
        self.Color = Color
        self.Year = Year

    def printData(self):

            print(self.Model)
            print(self.Color)
            print(self.Year)

    def getCustomer(self, name):

            self.name = name

    def getPrintcustomer(self):

            print(self.name)

bmw = Car("3 Series", "Red", "2022")
benz = Car("C Class", "White", "2021")

bmw.getCustomer("Dhanush")
bmw.getPrintcustomer()
