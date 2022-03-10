class Birds:

    def fly(self):
        print("All Birds can Fly")

class Pigeon(Birds):

    def fly(self):
        super().fly()  # super is a keyword that specifies the printing of any functions.
        print("Pigeon can Fly")

ob = Pigeon()
ob.fly()