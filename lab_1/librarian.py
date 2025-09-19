from lab_1.abstact_ridebike import RideBike
from person import Person

class Librarian(Person, RideBike):

    def ride_bike(self):
        return f"{self} катається на велосипеді"
